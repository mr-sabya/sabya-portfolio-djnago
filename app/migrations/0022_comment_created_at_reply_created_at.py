# Generated by Django 4.2.2 on 2023-07-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_userinfo_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]