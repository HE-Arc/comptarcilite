# Generated by Django 3.0.3 on 2020-03-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptarciliteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='id_account',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='id_user',
            new_name='user',
        ),
    ]
