# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='CompanyFlat',
            new_name='LocationCompanyCity',
        ),
        migrations.RemoveField(
            model_name='locationcompanycity',
            name='flat',
        ),
        migrations.AddField(
            model_name='flat',
            name='address',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationcompanycity',
            name='location',
            field=models.ForeignKey(default=1, to='Core.Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bhk',
            name='bhk',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flat',
            name='location',
            field=models.ForeignKey(to='Core.Location'),
            preserve_default=True,
        ),
    ]
