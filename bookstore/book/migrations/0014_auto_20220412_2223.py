# Generated by Django 3.0 on 2022-04-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20220412_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Category',
        ),
        migrations.AddField(
            model_name='book',
            name='Edition',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Science'), ('2', 'Poetry'), ('3', 'Art'), ('4', 'Philosophy')], max_length=80, null=True),
        ),
    ]