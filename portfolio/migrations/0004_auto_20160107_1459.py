# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_medium_project_project_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project_name',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='detail_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='disciplines',
        ),
        migrations.RemoveField(
            model_name='project',
            name='in_development',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='project',
            name='media',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='overview_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_url',
        ),
        migrations.AddField(
            model_name='project',
            name='projectdate',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='projectimage',
            field=models.ImageField(upload_to=None, default='https://pmcdeadline2.files.wordpress.com/2010/08/nicolas_cage.jpg'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectmedium',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='projecttext',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='projecttitle',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterModelTable(
            name='project',
            table=None,
        ),
        migrations.DeleteModel(
            name='Medium',
        ),
    ]
