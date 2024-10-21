from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('service/<int:pk>', views.service),
    path('serve/<int:pk>', views.serve),
    path('about/', views.about),
    path('survey/', views.survey)
]