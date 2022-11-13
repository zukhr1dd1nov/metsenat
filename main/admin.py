from django.contrib import admin
from main.models import Sponsor, Student, StudentBudget, University


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['person', 'full_name', 'phone', 'budget']
    list_display_links = ['person', 'full_name', 'phone', 'budget']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'university', 'student_type', 'request', 'send']
    list_display_links = ['full_name', 'university', 'student_type', 'request', 'send']
    search_fields = ['full_name']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(StudentBudget)
class StudentBudgetAdmin(admin.ModelAdmin):
    list_display = ['student', 'sponsor', 'money',]
    list_display_links = ['student', 'sponsor', 'money']
