# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0002_feed_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.CharField(default=b'linking parking', max_length=50),
        ),
        migrations.AddField(
            model_name='track',
            name='title',
            field=models.CharField(default=b'in the end', max_length=50),
        ),
        migrations.AddField(
            model_name='track',
            name='uri',
            field=models.CharField(default=b'localhost', max_length=100),
        ),
    ]
