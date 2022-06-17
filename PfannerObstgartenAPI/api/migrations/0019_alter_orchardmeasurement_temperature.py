# Generated by Django 4.0.4 on 2022-06-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_labmeasurement_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orchardmeasurement',
            name='temperature',
            field=models.CharField(blank=True, choices=[('Kalt', 'Kalt'), ('Mittel', 'Mittel'), ('Warm', 'Warm')], max_length=30, null=True),
        ),
    ]
