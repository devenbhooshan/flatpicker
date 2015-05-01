# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0016_auto_20150430_0506'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationcompanycity',
            unique_together=set([('location', 'company', 'city', 'area')]),
        ),
    ]
