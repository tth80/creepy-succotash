# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('PL', 'Planning')], max_length=2, default='PE'),
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='subtype',
            field=models.ForeignKey(to='planner.TaskSubtype', related_name='statuses+'),
        ),
        migrations.AddField(
            model_name='task',
            name='subtype',
            field=models.ForeignKey(to='planner.TaskSubtype', default=None, related_name='tasks+'),
            preserve_default=False,
        ),
    ]
