# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_lesson_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sheetFile', models.FileField(upload_to='sheets/')),
                ('lesson', models.ForeignKey(to='app.Lesson')),
                ('uploadedBy', models.OneToOneField(to='app.Student')),
            ],
        ),
    ]
