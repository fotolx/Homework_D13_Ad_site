# Generated by Django 4.2 on 2023-06-23 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads_for_sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
