# Generated by Django 3.1.4 on 2021-03-31 10:31

import apps.user.models.profile
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210326_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=apps.user.models.profile.get_upload_path),
        ),
    ]
