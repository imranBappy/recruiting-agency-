from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.country, name='country_jobs'),
    path('countries/', views.countries, name='countries'),
]