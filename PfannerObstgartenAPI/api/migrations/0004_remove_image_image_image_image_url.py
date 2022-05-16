# Generated by Django 4.0.4 on 2022-05-16 12:00

import api.models.Image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
