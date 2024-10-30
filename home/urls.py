from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('service/<int:pk>', views.service),
    path('serve/<int:pk>', views.serve),
    path('about/', views.about),
    path('survey/', views.survey),
    path('our-clients/', views.our_client),
    path('our-strength/', views.our_strength),
    path('corporate-structure/', views.corporate_structure),
    path('management-team/', views.team_management),
    path('recruitment-process/', views.recruitment_process),
    path('quick-register/', views.quick_register),
    path('terms/', views.quick_register),

]

