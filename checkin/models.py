from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=2048)
    create_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=64, blank=True)
    wechat = models.CharField(max_length=64, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Checkin(models.Model):
    event = models.ForeignKey(Event)
    contact = models.ForeignKey(Contact)
    create_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
