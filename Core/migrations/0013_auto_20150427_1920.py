# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_locationcompanycity_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
