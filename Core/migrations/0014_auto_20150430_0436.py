# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_auto_20150427_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='crawled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='crawled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
