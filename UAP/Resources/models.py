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



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

