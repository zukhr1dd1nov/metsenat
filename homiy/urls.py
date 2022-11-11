from django.urls import path
from .views import SponsorCreateView, SponsorDetailView, SponsorListView

urlpatterns = [
    path('', SponsorListView.as_view()),
    path('create/', SponsorCreateView.as_view()),
    path('<int:pk>/', SponsorDetailView.as_view()),
]
