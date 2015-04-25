# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_latlong'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
