# Generated by Django 4.2.3 on 2023-11-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0005_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.TextField(default=''),
        ),
    ]