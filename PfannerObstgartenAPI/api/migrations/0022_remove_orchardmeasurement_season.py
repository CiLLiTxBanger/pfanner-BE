# Generated by Django 4.0.4 on 2022-06-20 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_orchardmeasurement_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orchardmeasurement',
            name='season',
        ),
    ]