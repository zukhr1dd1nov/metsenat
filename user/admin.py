from django.contrib import admin
from user.models import SponsorModel, StudentModel, StudentBudgetModel, UniversityModel


@admin.register(SponsorModel)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['person', 'full_name', 'phone_number', 'budget']
    list_display_links = ['person', 'full_name', 'phone_number', 'budget']


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'university', 'student_type', 'request', 'send']
    list_display_links = ['full_name', 'phone', 'university', 'student_type', 'request', 'send']
    search_fields = ['full_name']


@admin.register(UniversityModel)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['university_name']
    list_display_links = ['university_name']
    search_fields = ['university_name']


@admin.register(StudentBudgetModel)
class StudentBudgetAdmin(admin.ModelAdmin):
    list_display = ['student', 'sponsor', 'money',]
    list_display_links = ['student', 'sponsor', 'money']
