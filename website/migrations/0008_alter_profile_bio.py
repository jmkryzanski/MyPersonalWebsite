# Generated by Django 4.0 on 2022-01-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_delete_profile2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='hello world', max_length=10000),
        ),
    ]