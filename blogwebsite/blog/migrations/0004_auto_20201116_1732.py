# Generated by Django 3.1.1 on 2020-11-16 12:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201116_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
