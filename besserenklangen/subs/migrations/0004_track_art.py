# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0003_auto_20151129_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='art',
            field=models.CharField(default=b'http://i.imgur.com/BNBFGfg.jpg', max_length=100),
        ),
    ]
