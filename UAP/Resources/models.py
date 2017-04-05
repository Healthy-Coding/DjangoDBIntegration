from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()

    def get_absolute_url(self):
        return "/resources/%s/" % self.post_id


