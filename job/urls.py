from django.urls import path
from . import views


urlpatterns = [
    path('<int:country_pk>/<int:job_pk>/', views.job_details, name='job_details'),
    path('apply-job/<int:job_pk>', views.apply_resume, name='apply_resume'),
    path('apply-job/submit/<int:job_pk>/', views.apply_resume_summit, name='apply_resume_submit'),
    path('success/', views.success, name='success'),
    path('jobseeker/', views.candidate, name='jobseeker'),
    path('clients/', views.clients, name='clients'),
    path('clients/submit', views.clients_submit, name='clients_submit'),

    path('jobseeker/submit', views.candidate_submit, name='jobseeker_submit'),
    path('employee/', views.employee, name='employee'),
    path('employee/submit', views.employee_submit, name='employee_submit'),
    path('study/', views.study, name='study'),
    path('study/submit', views.study_submit, name='study_submit'),
    path('grievance-redressal/', views.grievance, name='grievance'),
    path('grievance-redressal/submit', views.grievance_submit, name='grievance_submit'),
    path('careers', views.createJobList, name='careers_job_list'),
    path('careers/<int:job_pk>', views.job_detailsViewLoggedIn, name='job_detailsViewLoggedIn'),
    path('careers/apply/<int:job_pk>', views.apply_resumeViewLoggedIn, name='apply_resumeViewLoggedIn'),
    path('save/<int:job_pk>', views.save_job_view, name='save_job_view'),
    path('application/', views.application, name='application'),
    path('save/', views.save, name='save'),
    path('update-picture/', views.update_profile_picture , name="update_profile_picture" )
]
