# Generated by Django 4.2.3 on 2023-11-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0007_alter_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='imageUrl',
            field=models.CharField(max_length=500),
        ),
    ]
