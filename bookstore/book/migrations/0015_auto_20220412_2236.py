# Generated by Django 3.0 on 2022-04-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20220412_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Mystery & Thriller'), ('2', 'History'), ('3', 'Romance'), ('4', 'Childeren & Young Adults'), ('5', 'Literature & Fiction'), ('6', 'Biographies'), ('7', 'Business'), ('8', 'Health'), ('9', 'art')], max_length=80, null=True),
        ),
    ]
