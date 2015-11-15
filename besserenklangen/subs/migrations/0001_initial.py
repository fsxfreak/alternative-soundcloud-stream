# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='tracks',
            field=models.ManyToManyField(to='subs.Track'),
        ),
    ]
