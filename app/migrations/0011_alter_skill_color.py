# Generated by Django 4.2.2 on 2023-06-20 12:51

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_skill_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
    ]
