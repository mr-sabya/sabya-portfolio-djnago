# Generated by Django 4.2.2 on 2023-06-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_skill_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='color',
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(upload_to='skill/'),
        ),
    ]