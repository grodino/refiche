# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_teacher_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='firstName',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
