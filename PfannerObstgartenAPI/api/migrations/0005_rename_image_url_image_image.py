# Generated by Django 4.0.4 on 2022-05-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_image_image_image_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='image',
        ),
    ]
