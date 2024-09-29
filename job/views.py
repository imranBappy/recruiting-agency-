from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from country.models import Country
from .models import Job, ApplyJob,Candidate
from django.forms.models import model_to_dict
from .forms import ApplyJobForm,CandidateForm,EmployeeForm, StudyForm, GrievanceForm
from django.views.decorators.http import require_http_methods
from home.models import Contact, Setting, Service




def job_details(request, country_pk, job_pk):
    country = get_object_or_404(Country, id=country_pk)
    job  = get_object_or_404(Job, id=job_pk)
    jobs = country.jobs.all()
    job_dist = model_to_dict(job)
    del job_dist['country']

    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
  
    context= {
        'job': job_dist,
        "jobs":jobs,
        "jobId" : job_dist['id'],
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
    }

    template = loader.get_template("job_details.html")
    return HttpResponse(template.render(context))


@require_http_methods(['GET'])
def apply_resume(request, job_pk):
    job  = get_object_or_404(Job, id=job_pk)
    form = ApplyJobForm()
    return render(request, 'apply_job.html', {'job': job,})



@require_http_methods(['POST'])
def apply_resume_summit(request, job_pk):
    job  = get_object_or_404(Job, id=job_pk)
    form = ApplyJobForm(request.POST, request.FILES)
    if form.is_valid():
        job_apply  = form.save(commit=False)  
        job_apply.job = job
        job_apply.save()
        return redirect('success')
    return render(request, 'apply_job.html', {'job': job})


def success(request):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
    }
    return  render(request, 'success.html',context)


@require_http_methods(['GET'])
def candidate(request):
    form = CandidateForm()
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
        "form":form,
    }
    return render(request,"jobseeker.html" , context)


@require_http_methods(['POST'])
def candidate_submit(request):
    form = CandidateForm(request.POST,request.FILES )
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,"jobseeker.html" , {"form":form})



@require_http_methods(['GET'])
def employee(request):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
    }

    return render(request,"employee.html",context )



@require_http_methods(['POST'])
def employee_submit(request):
    form = EmployeeForm(request.POST)
    print(form.is_valid(),form.errors, form.cleaned_data)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,"employee.html" )



@require_http_methods(['GET'])
def study(request):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
    }
    return render(request,"study.html",context )

@require_http_methods(['POST'])
def study_submit(request):
    form = StudyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,"study.html" )

@require_http_methods(['GET'])
def grievance(request):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
    }
    return render(request,"grievance.html",context )

@require_http_methods(['POST'])
def grievance_submit(request):
    form = GrievanceForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,"grievance.html" )