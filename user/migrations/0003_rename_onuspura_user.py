# Generated by Django 5.0.3 on 2024-04-21 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0002_rename_user_onuspura'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='onuspura',
            new_name='User',
        ),
    ]