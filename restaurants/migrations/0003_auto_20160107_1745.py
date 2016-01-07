# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20160105_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='album',
            field=models.ForeignKey(blank=True, null=True, to='restaurants.Photo'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, to='restaurants.Review'),
        ),
    ]
