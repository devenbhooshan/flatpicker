# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_auto_20150425_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatLong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
                ('area', models.ForeignKey(to='Core.Area')),
                ('city', models.ForeignKey(to='Core.City')),
                ('company', models.ForeignKey(to='Core.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
