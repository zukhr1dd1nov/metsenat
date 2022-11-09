# Generated by Django 4.1.3 on 2022-11-08 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('person', models.IntegerField(choices=[('Yuridik', 1), ('Jismoniy', 2)], verbose_name='shaxs turi')),
                ('full_name', models.CharField(max_length=255, verbose_name='F.I.Sh')),
                ('phone_number', models.CharField(max_length=255, verbose_name='telefon raqam')),
                ('name_company', models.CharField(blank=True, max_length=255, null=True, verbose_name='Firma nomi')),
                ('condition', models.IntegerField(choices=[('Yangi', 1), ('Tasdiqlanmagan', 2), ('Moderatsiyada', 3), ('Bekor qilingan', 4)], verbose_name='Holat')),
                ('budget', models.PositiveIntegerField(default=1000000)),
            ],
            options={
                'verbose_name': 'Homiy',
                'verbose_name_plural': 'Homiylar',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('university_name', models.CharField(max_length=255, verbose_name='Universitetning Nomi')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universitet',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='F.I.SH')),
                ('phone', models.CharField(max_length=255, verbose_name='telefon raqam')),
                ('student_type', models.IntegerField(choices=[('Bakalavr', 1), ('Magistratura', 2), ('Aspirantura', 3)], verbose_name='Talim turi')),
                ('request', models.PositiveIntegerField(verbose_name='Soralgan pul miqdori')),
                ('send', models.PositiveIntegerField(verbose_name='Tolangan pul miqdori')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.university', verbose_name='Institut')),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
            },
        ),
        migrations.CreateModel(
            name='StudentBudgetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('money', models.PositiveIntegerField(verbose_name='Pull miqdori')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.sponsormodel', verbose_name='Homiy')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.studentmodel', verbose_name='Talaba')),
            ],
            options={
                'verbose_name': 'Talaba va Homiy',
                'verbose_name_plural': 'Talabalar va Homiylar',
            },
        ),
    ]
