# Generated by Django 3.2.5 on 2021-08-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_finished_upcoming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='upcoming',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='upcoming',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
