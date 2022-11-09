from django.urls import path
from .views import ListSponsorView

urlpatterns = [
    path('sponsors/', ListSponsorView.as_view())
]