# Generated by Django 3.2.5 on 2021-08-31 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210831_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='future',
            name='release',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
