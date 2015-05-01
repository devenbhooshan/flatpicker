# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_auto_20150430_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='address',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flat',
            name='bhk',
            field=models.FloatField(max_length=10),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='BHK',
        ),
    ]
