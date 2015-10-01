from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    body = models.TextField(default='')

    tags = TaggableManager(blank=True)

    author = models.ForeignKey(User, related_name='posts+')
    editor = models.ForeignKey(User, related_name='editors+', blank=True,
                               null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})
