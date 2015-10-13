# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0008_plan_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksubtype',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
