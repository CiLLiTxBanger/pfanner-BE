# Generated by Django 4.0.4 on 2022-06-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_variety_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='image_description',
            field=models.TextField(blank=True, default=None, max_length=180, null=True),
        ),
    ]
