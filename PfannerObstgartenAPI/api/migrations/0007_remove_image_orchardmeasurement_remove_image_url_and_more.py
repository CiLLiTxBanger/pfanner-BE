# Generated by Django 4.0.4 on 2022-05-19 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_image_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='orchardMeasurement',
        ),
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.RemoveField(
            model_name='image',
            name='variety',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='orchardmeasurement',
            name='photo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.image'),
        ),
        migrations.AddField(
            model_name='variety',
            name='photo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]