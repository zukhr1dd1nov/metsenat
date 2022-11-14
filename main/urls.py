from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainListView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('sponsors/create/', SponsorCreateView.as_view()),
    path('sponsors/<int:pk>/', SponsorDetailView.as_view()),
]

