# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20150423_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhk',
            name='bhk',
            field=models.FloatField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='locationcompanycity',
            unique_together=set([('location', 'company', 'city')]),
        ),
    ]
