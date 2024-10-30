from django.contrib import admin
from .models import Job, ApplyJob, Candidate, Study, Employee,Grievance, CurrentLocation
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    # list_display=("title","job_type", "city","state","zip_code","description","country")
    pass

@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    pass

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    pass

@admin.register(CurrentLocation)
class GrievanceAdmin(admin.ModelAdmin):
    pass