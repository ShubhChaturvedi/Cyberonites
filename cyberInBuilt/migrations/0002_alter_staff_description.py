# Generated by Django 4.0.5 on 2022-08-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyberInBuilt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]