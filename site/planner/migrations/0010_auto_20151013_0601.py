# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0009_tasksubtype_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together=set([('author', 'slug')]),
        ),
    ]
