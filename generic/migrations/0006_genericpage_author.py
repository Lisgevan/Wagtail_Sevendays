# Generated by Django 3.2.4 on 2021-06-08 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0005_rename_company_nurl_author_company_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='generic.author'),
        ),
    ]
