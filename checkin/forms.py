# -*- coding: utf-8 -*-
from django import forms


class EventForm(forms.Form):
    name = forms.CharField(max_length=64)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=64)
    phone = forms.CharField(max_length=64)
    wechat = forms.CharField(max_length=64)
