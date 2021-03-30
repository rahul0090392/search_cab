# Generated by Django 3.1 on 2021-01-23 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='row_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='row_last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
