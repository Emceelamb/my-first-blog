# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'media',
                'verbose_name_plural': 'media',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('project_url', models.URLField(verbose_name='Project URL')),
                ('description', models.TextField(blank=True)),
                ('disciplines', models.CharField(max_length=200)),
                ('completion_date', models.DateField()),
                ('in_development', models.BooleanField()),
                ('is_public', models.BooleanField(default=True)),
                ('overview_image', models.URLField()),
                ('detail_image', models.URLField()),
                ('media', models.ManyToManyField(to='portfolio.Medium')),
            ],
            options={
                'db_table': 'projects',
                'ordering': ['-completion_date'],
            },
        ),
        migrations.CreateModel(
            name='Project_name',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'name',
                'ordering': ['name'],
            },
        ),
    ]
