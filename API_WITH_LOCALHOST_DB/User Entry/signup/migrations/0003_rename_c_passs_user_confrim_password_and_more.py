# Generated by Django 4.0.1 on 2022-01-27 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_rename_users_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='C_passs',
            new_name='Confrim_password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Passwd',
            new_name='Password',
        ),
    ]
