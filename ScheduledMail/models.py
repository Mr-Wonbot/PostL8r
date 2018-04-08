from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class ScheduledMail(models.Model):
    recipient = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    setDelivery = models.DateTimeField()

    def __str__(self):
        return self.subject
