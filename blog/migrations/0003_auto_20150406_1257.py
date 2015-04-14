# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de parution'),
        ),
    ]
