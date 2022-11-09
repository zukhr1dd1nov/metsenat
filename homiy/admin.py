from django.contrib import admin
from user.models import SponsorModel


@admin.register(SponsorModel)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['person', 'full_name', 'phone_number', 'budget']
    list_display_links = ['person', 'full_name', 'phone_number', 'budget']


