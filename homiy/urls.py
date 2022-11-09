from django.urls import path
from .views import SponsorCreateView, SponsorDetailView

urlpatterns = [
    path('', SponsorCreateView.as_view()),
    path('<int:pk>/', SponsorDetailView.as_view()),
]
