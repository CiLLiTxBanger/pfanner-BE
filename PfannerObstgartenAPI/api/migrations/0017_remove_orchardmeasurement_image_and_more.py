# Generated by Django 4.0.4 on 2022-06-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_variety_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orchardmeasurement',
            name='image',
        ),
        migrations.AddField(
            model_name='orchardmeasurement',
            name='image_description',
            field=models.TextField(blank=True, default=None, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='orchardmeasurement',
            name='image_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
