from .views import *
from django.urls import path

urlpatterns = [
    path('<int:pk>/',DetailToDO.as_view()),
    path('',ListToDO.as_view()),
    path('create',CreateToDO.as_view()),
    path('delete/<int:pk>/',DeleteToDO.as_view())
]
