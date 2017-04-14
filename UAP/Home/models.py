from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=120)
    content = models.TextField()
    sender = models.EmailField(max_length=255, blank=True, null=True)
    timesent = models.DateTimeField("Time Sent")
    resolved = models.BooleanField(default=False)

    class Meta:
        db_table = 'Contact'
