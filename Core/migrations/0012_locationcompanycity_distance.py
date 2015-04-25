# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_flat_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationcompanycity',
            name='distance',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
