# Generated by Django 4.2.2 on 2023-06-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='details',
            field=models.TextField(max_length=255),
        ),
    ]