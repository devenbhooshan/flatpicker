# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_company_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='furnished',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
