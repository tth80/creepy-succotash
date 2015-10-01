# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_taskstatus_default_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
