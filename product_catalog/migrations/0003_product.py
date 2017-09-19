# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0002_remove_category_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the entry's URL.", max_length=255, unique_for_date=b'publication_date', verbose_name='slug')),
                ('publication_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='publication date')),
                ('start_publication', models.DateTimeField(blank=True, db_index=True, help_text='Start date of publication.', null=True, verbose_name='start publication')),
                ('end_publication', models.DateTimeField(blank=True, db_index=True, help_text='End date of publication.', null=True, verbose_name='end publication')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last update')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('categories', models.ManyToManyField(blank=True, related_name='entries', to='product_catalog.Category', verbose_name='categories')),
            ],
            options={
                'get_latest_by': 'publication_date',
                'ordering': ['-publication_date'],
                'abstract': False,
                'verbose_name_plural': 'products',
                'verbose_name': 'product',
            },
        ),
    ]
