# Generated by Django 3.0 on 2022-04-12 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220412_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='customer',
        ),
    ]
