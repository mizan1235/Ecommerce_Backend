# Generated by Django 4.2.3 on 2023-08-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_alter_products_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_cred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=22)),
            ],
        ),
    ]
