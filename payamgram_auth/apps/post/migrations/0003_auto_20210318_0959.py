# Generated by Django 3.1.4 on 2021-03-18 06:29

import apps.post.models.post
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210317_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=apps.post.models.post.get_upload_path),
        ),
    ]
