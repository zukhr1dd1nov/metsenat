from django.urls import path
from .views import SponsorDetailView

urlpatterns = [
    path('sponsor/', SponsorDetailView.as_view({'get': 'list'}))
]