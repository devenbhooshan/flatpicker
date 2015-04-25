# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_flat_furnished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='area',
            new_name='size',
        ),
    ]
