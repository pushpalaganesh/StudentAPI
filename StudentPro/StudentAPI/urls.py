from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentView),
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),
]
