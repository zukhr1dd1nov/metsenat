from django.db import models
from optparse import Values
from django.dispatch import receiver
from django.forms import IntegerField
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from rest_framework.exceptions import ValidationError


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class University(BaseModel):
    name = models.CharField("Universitetning Nomi", max_length=255)

    def __str__(self):
        return self.name

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
    (2, 'Tasdiqlangan'),
    (3, 'Moderatsiyada'),
    (4, 'Bekor qilingan'),
]


class Sponsor(BaseModel):
    is_phisical_person = models.BooleanField('Shaxs turi', choices=PERSON)
    full_name = models.CharField('F.I.Sh', max_length=255)
    phone = models.CharField('telefon raqam', max_length=9)
    name_company = models.CharField('Firma nomi', max_length=255, blank=True, null=True)
    condition = models.IntegerField('Holat', choices=CONDITIONS, default=1)
    budget = models.PositiveIntegerField()
    used = models.PositiveIntegerField(default=0)
    is_counted = models.BooleanField(default=False)

    @property
    def remaining_budget(self):
        return self.budget - self.used
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


class Student(BaseModel):
    full_name = models.CharField("F.I.SH", max_length=255)
    phone = models.CharField('telefon raqam', max_length=9)
    university = models.ForeignKey(University, verbose_name='Institut', on_delete=models.RESTRICT)
    student_type = models.IntegerField('Talim turi', choices=TYPE)
    request = models.PositiveIntegerField('Soralgan pul miqdori')
    send = models.PositiveIntegerField('Tolangan pul miqdori', default=0)

    @property
    def remaining_request(self):
        return self.request-self.send

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class StudentBudget(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, verbose_name='Talaba')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.RESTRICT, verbose_name='Homiy')
    money = models.PositiveIntegerField(verbose_name='Pull miqdori')

    def __str__(self):
        return f"{self.student}  {self.sponsor}"

    class Meta:
        verbose_name = 'Talaba va Homiy'
        verbose_name_plural = 'Talabalar va Homiylar'


class LinearGraph(models.Model):
    number_sp = models.PositiveIntegerField(default=0)
    number_st = models.PositiveIntegerField(default=0)
    day = models.DateField()

    def __str__(self):
        return f'{self.day}'

    class Meta:
        verbose_name = 'Kunlik Statistika'
        verbose_name_plural = 'Kunlar Statistikasi'

class MainDatas(models.Model):
    money_asked = models.PositiveIntegerField(default=0)
    money_sent = models.PositiveIntegerField(default=0)
    money_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"So'raldi:  {self.money_asked} Berildi:  {self.money_sent}  Bor:  {self.money_amount}"

    class Meta:
        verbose_name = 'Asosiy Malumotlar'
        verbose_name_plural = 'Asosiy Malumotlar'