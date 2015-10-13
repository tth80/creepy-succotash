# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0010_auto_20151013_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksubtype',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
