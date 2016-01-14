# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20160107_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published', blank=True),
        ),
    ]
