# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20151001_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(to='planner.TaskStatus', default=None, related_name='tasks2+'),
            preserve_default=False,
        ),
    ]
