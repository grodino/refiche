# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_student_isdelegate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lessons',
            field=models.ManyToManyField(to='app.Lesson', null=True),
        ),
    ]
