# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationcompanycity',
            name='area',
            field=models.ForeignKey(default=1, to='Core.Area'),
            preserve_default=True,
        ),
    ]
