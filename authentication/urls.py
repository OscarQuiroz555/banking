from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('countries/', views.Country, name='country'),
    path('departments/', views.Department, name='department'),
    path('cities/', views.City, name='city'),
]

