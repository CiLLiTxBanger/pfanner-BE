# Generated by Django 4.0.4 on 2022-06-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_remove_orchardmeasurement_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orchardmeasurement',
            name='lateFrost',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=30, null=True),
        ),
    ]