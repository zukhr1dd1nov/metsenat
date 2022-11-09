from django.db import models
from optparse import Values
from django.dispatch import receiver
from django.forms import IntegerField
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from rest_framework.exceptions import ValidationError

from user.validators import min_contribution


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UniversityModel(BaseModel):
    university_name = models.CharField("Universitetning Nomi", max_length=255)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universitet'


# Sponsor
PERSON = [
    (0, 'Yuridik'),
    (1, 'Jismoniy'),
]

CONDITIONS = [
    (1, 'Yangi'),
    (2, 'Tasdiqlanmagan'),
    (3, 'Moderatsiyada'),
    (4, 'Bekor qilingan'),
]


class SponsorModel(BaseModel):
    person = models.BooleanField('Shaxs turi', choices=PERSON)
    full_name = models.CharField('F.I.Sh', max_length=255)
    phone_number = models.CharField('telefon raqam', max_length=9)
    name_company = models.CharField('Firma nomi', max_length=255, blank=True, null=True)
    condition = models.IntegerField('Holat', choices=CONDITIONS, default=1)
    budget = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Homiy'
        verbose_name_plural = 'Homiylar'


# STUDENTS
TYPE = [
    (1, 'Bakalavr'),
    (2, 'Magistratura'),
    (3, 'Aspirantura'),
]


class StudentModel(BaseModel):
    full_name = models.CharField("F.I.SH", max_length=255)
    phone_number = models.CharField('telefon raqam', max_length=9)
    university = models.ForeignKey(UniversityModel, verbose_name='Institut', on_delete=models.RESTRICT)
    student_type = models.IntegerField('Talim turi', choices=TYPE)
    request = models.PositiveIntegerField('Soralgan pul miqdori')
    send = models.PositiveIntegerField('Tolangan pul miqdori')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class StudentBudgetModel(BaseModel):
    student = models.ForeignKey(StudentModel, on_delete=models.RESTRICT, verbose_name='Talaba')
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.RESTRICT, verbose_name='Homiy')
    money = models.PositiveIntegerField(verbose_name='Pull miqdori')

    def __str__(self):
        return f"{self.student}  {self.sponsor}"

    class Meta:
        verbose_name = 'Talaba va Homiy'
        verbose_name_plural = 'Talabalar va Homiylar'


