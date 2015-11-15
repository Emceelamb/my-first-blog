# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151114_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('projecttitle', models.CharField(max_length=200)),
                ('projectdate', models.CharField(max_length=200)),
                ('projectmedium', models.CharField(max_length=200)),
                ('projecttext', models.TextField()),
            ],
        ),
    ]
