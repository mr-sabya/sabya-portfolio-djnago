# Generated by Django 4.2.2 on 2023-06-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_client_details_alter_project_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_image',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
