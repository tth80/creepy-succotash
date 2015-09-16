# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='posts+', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(related_name='editors+', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
        ),
    ]
