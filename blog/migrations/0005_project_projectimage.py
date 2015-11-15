# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectimage',
            field=models.ImageField(upload_to=None, default=datetime.datetime(2015, 11, 15, 7, 46, 30, 789822, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
