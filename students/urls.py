from django.urls import path
from .views import StudentCreateView, StudentBudgetView, StudentDetailView, StudentListView

urlpatterns = [
    path('', StudentListView.as_view()),
    path('create/', StudentCreateView.as_view()),
    path('budget/', StudentBudgetView.as_view()),
    path('<int:pk>/', StudentDetailView.as_view()),
]
