# Generated by Django 3.2.4 on 2021-06-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]