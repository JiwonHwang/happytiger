# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20160107_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='email',
            field=models.ForeignKey(null=True, to='restaurants.Email', blank=True),
        ),
    ]
