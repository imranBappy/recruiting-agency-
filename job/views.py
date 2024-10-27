from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from country.models import Country
from .models import Job, ApplyJob,Candidate, Save,Client
from django.forms.models import model_to_dict
from .forms import ApplyJobForm,CandidateForm,EmployeeForm, StudyForm, GrievanceForm, ClientForm
from django.views.decorators.http import require_http_methods
from home.models import Contact, Setting, Service
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from user.models import UserProfile


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
    form = ApplyJobForm()
    job  = get_object_or_404(Job, id=job_pk)
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    countries = Country.objects.all()

    return render(request, 'apply_job.html', {'job': job, 'countries':countries,    'contact':contact,'settings':settings,})



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

@require_http_methods(['GET'])
def clients(request):
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
    return render(request,"client.html" , context)

@require_http_methods(['POST'])
def clients_submit(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,"client.html" )

@require_http_methods(['POST'])
def candidate_submit(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    whatsApp = request.POST.get('whatsApp')
    email = request.POST.get('email')
    category = request.POST.get('category')
    position = request.POST.get('position')
    location_id = request.POST.get('location')
    agreed = request.POST.get('agreed') == 'on'  # Checkbox is 'on' if checked, otherwise absent

    # File handling for 'resume'
    resume_file = request.FILES.get('resume')

    form = CandidateForm(request.POST,request.FILES )
    if form.is_valid():
        # form.save()
        candidate = Candidate(
            name=name,
            phone=phone,
            whatsApp=whatsApp,
            email=email,
            category=category,
            position=position,
            location_id=location_id,
            agreed=agreed  
        )
        if resume_file:
            candidate.resume = resume_file
        candidate.save()
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


@require_http_methods(["GET"])
def createJobList(request):
    query = request.GET.get("job_search","")
    query2 = request.GET.get("location")
    job_type = request.GET.get("job_type", "")  

    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    services = Service.objects.all()



    filter_query = Q()
    if query:
        filter_query |= Q(title__icontains=query)
    if query2:
        filter_query |= Q(city__icontains=query2) | Q(country__name__icontains=query2)
    if job_type:  # If a job type is selected, filter by job_type
        filter_query &= Q(job_type=job_type)
    jobs = Job.objects.filter(filter_query) if query or query2 or job_type else Job.objects.all()


    context= {
        'jobs':jobs,
        'contact':contact,
        'settings':settings,
        'services':services,
        'job_type': "true" if job_type else ""
    }
    return render(request, "careers.html", context)



@login_required(login_url='/login/')
def job_detailsViewLoggedIn(request,  job_pk ):
    job  = get_object_or_404(Job, id=job_pk)
    country = get_object_or_404(Country, id=job.country.id)
    user = request.user
    existing_save = Save.objects.filter(user=request.user, job=job).first()

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
        'is_saved': existing_save is not None 
    }

    
    return render(request, "job_details2.html", context)


@login_required(login_url='/login/')
def apply_resumeViewLoggedIn(request, job_pk):
    job  = get_object_or_404(Job, id=job_pk)

    if(request.method== 'POST'):
        form = ApplyJobForm(request.POST, request.FILES)
        if form.is_valid():
            job_apply  = form.save(commit=False)  
            job_apply.user = request.user
            job_apply.job = job
            job_apply.save()
            return redirect('/careers')
    user = request.user
    profile =  UserProfile.objects.get(user=user)
    return render(request, 'apply_job2.html', {'job': job, 'profile':profile})



@login_required(login_url='/login/')
def save_job_view(request, job_pk):
    job = get_object_or_404(Job, id=job_pk)
    # Check if the job is already saved by the user
    existing_save = Save.objects.filter(user=request.user, job=job).first()
    if request.method == 'POST':
        if existing_save:
            existing_save.delete()
            return redirect('job_detailsViewLoggedIn', job_pk)  # Redirect back to job detail page
        else:
            # Save the job for the user
            save_entry = Save(user=request.user, job=job)
            save_entry.save()
            return redirect('job_detailsViewLoggedIn', job_pk)  # Redirect back to job detail page

    return redirect('job_detailsViewLoggedIn', job_pk)



    user = request.user
    profile = UserProfile.objects.get(user=user)
    
    return render(request, 'application.html',
    {'user': user, 'profile': profile}
    )

@login_required(login_url='/login/')
def application(request):

    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    services = Service.objects.all()
    
    jobs = ApplyJob.objects.filter(user = request.user)
    profile = UserProfile.objects.get(user=request.user)

    context= {
        'profile':profile,
        'jobs':jobs,
        'contact':contact,
        'settings':settings,
        'services':services,
    }
    return render(request, "application.html", context)


@login_required(login_url='/login/')
def save(request):

    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    services = Service.objects.all()
    
    jobs = Save.objects.filter(user = request.user)
    profile = UserProfile.objects.get(user=request.user)

    context= {
        'profile':profile,
        'jobs':jobs,
        'contact':contact,
        'settings':settings,
        'services':services,
    }
    return render(request, "save.html", context)


@login_required(login_url='/login/')
def update_profile_picture(request):
    if request.method == 'POST' and 'profile_pic' in request.FILES:
        profile_pic = request.FILES['profile_pic']
        print("check -> ", profile_pic)

        profile = UserProfile.objects.get(user= request.user.id)
        profile.img = profile_pic  # Assuming `profile_pic` is a field on your profile model
        profile.save() 
    return redirect('profile')