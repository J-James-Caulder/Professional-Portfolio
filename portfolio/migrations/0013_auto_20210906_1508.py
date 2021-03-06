# Generated by Django 3.2.5 on 2021-09-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_rename_demo_recording'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/media/'),
        ),
        migrations.AlterField(
            model_name='future',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sample',
            field=models.FileField(blank=True, upload_to='portfolio/media/'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='sample',
            field=models.FileField(blank=True, upload_to='portfolio/media/'),
        ),
    ]
