from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from checkin.models import Event, Contact, Checkin
from checkin.forms import EventForm, ContactForm


def home(request):
    events = Event.objects.order_by('-updated')
    return render(request, 'home.html', {'events': events})

def info(request, event_id):
    try:
        event = Event.objects.get(id = event_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    contacts = Contact.objects.order_by('name')
    for contact in contacts:
        try:
            Checkin.objects.get(event=event, contact=contact)
            contact.checked = True
        except ObjectDoesNotExist:
            contact.checked = False
    return render(request, 'info.html', {'event': event, 'contacts': contacts})


def post(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            event = Event.objects.create(name=name)
            event.save()
            print event.id, 'wala'
            return HttpResponseRedirect(reverse('info', args=[event.id]))
    else:
        form = EventForm()
    return render(request, 'post.html', {'form': form,})


def check(request, event_id, contact_id):
    try:
        event = Event.objects.get(id = event_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))

    try:
        contact = Contact.objects.get(id = contact_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('info', args=[event.id]))

    Checkin.objects.get_or_create(event=event, contact=contact)
    return HttpResponseRedirect(reverse('info', args=[event.id]))


def uncheck(request, event_id, contact_id):
    try:
        event = Event.objects.get(id = event_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))

    try:
        contact = Contact.objects.get(id = contact_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('info', args=[event.id]))

    try:
        checkin = Checkin.objects.get(event=event, contact=contact)
        checkin.delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(reverse('info', args=[event.id]))


def create_contact(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except ObjectDoesNotExist:
        event = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            wechat = form.cleaned_data['wechat']
            Contact.objects.create(name=name, email=email, phone=phone, wechat=wechat)
            if event:
                return HttpResponseRedirect(reverse('info', args=[event.id]))
            else:
                return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form, 'event':event})
