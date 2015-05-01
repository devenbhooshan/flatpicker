# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_auto_20150430_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='bhk',
            field=models.ForeignKey(to='Core.BHK', default=1),
            preserve_default=True,
        ),
    ]
