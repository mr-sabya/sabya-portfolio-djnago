# Generated by Django 4.2.2 on 2023-06-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(max_length=100),
        ),
    ]
