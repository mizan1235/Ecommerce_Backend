# Generated by Django 4.2.3 on 2023-08-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0007_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='idProduct',
            field=models.IntegerField(),
        ),
    ]
