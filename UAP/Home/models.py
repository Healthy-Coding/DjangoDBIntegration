from django.db import models

# Create your models here.


class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    sender = models.EmailField()