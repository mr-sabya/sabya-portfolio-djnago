# Generated by Django 4.2.2 on 2023-06-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_service_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to='skill/')),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
