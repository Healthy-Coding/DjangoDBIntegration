from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=120)
    content = models.TextField()
    sender = models.EmailField(blank=True, null=True)
    time_sent = models.DateTimeField()
