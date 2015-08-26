# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('levels', models.ManyToManyField(to='app.Level')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='classroom',
            field=models.ForeignKey(default=1, to='app.Classroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classroom',
            name='level',
            field=models.ForeignKey(default=1, to='app.Level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(default=1, to='app.School'),
            preserve_default=False,
        ),
    ]
