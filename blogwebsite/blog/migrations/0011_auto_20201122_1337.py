# Generated by Django 3.1.1 on 2020-11-22 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201122_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 13, 37, 1, 114295)),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 13, 37, 1, 114295)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=400),
        ),
    ]
