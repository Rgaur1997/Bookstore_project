# Generated by Django 3.0 on 2022-04-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220412_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(null=True, to='book.Book'),
        ),
    ]