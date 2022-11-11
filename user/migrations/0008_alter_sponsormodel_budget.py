# Generated by Django 4.1.3 on 2022-11-09 12:00

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_sponsormodel_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsormodel',
            name='budget',
            field=models.PositiveIntegerField(default=1000000, validators=[user.validators.min_contribution]),
        ),
    ]
