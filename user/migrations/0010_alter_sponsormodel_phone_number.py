# Generated by Django 4.1.3 on 2022-11-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_sponsormodel_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsormodel',
            name='phone_number',
            field=models.CharField(max_length=9, verbose_name='telefon raqam'),
        ),
    ]