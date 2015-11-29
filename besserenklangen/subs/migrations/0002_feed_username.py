# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='username',
            field=models.CharField(default='fsxfreak', max_length=100),
            preserve_default=False,
        ),
    ]
