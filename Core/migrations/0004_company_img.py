# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_auto_20150424_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='img',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
