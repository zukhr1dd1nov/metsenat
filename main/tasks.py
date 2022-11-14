from config.celery import app
from .models import LinearGraph, Sponsor, Student, MainDatas
import datetime


@app.task
def create_data_graph():
    yesterday = datetime.date.today()
    number_sp = Sponsor.objects.filter(created_at__month=yesterday.month, created_at__day=yesterday.day, created_at__year=yesterday.year).count()
    number_st = Student.objects.filter(created_at__month=yesterday.month, created_at__day=yesterday.day, created_at__year=yesterday.year).count()
    LinearGraph.objects.create(day=yesterday, number_st=number_st, number_sp=number_sp)


@app.task
def money_management(sponsor, student, money):
    sponsor.used += money
    sponsor.save()
    student.send += money
    student.save()
    main_data = MainDatas.objects.get(id=1)
    main_data.money_sent += money
    main_data.save()


@app.task
def money_given(money):
    main_data = MainDatas.objects.get(id=1)
    main_data.money_amount += money
    main_data.save()


@app.task
def money_is_needed(money):
    main_data = MainDatas.objects.get(id=1)
    main_data.money_asked += money
    main_data.save()
