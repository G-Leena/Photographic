# Generated by Django 4.2.3 on 2023-07-31 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MYapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mobile',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='mobile',
            new_name='phone',
        ),
    ]
