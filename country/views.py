from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Country as CountryModel
from django.views.decorators.http import require_http_methods
from home.models import Slider, Award, Video, Serve, Contact, Setting, Service
# Create your views here.


def country(request, pk):
    query = request.GET.get("job_search","")
    country = get_object_or_404(CountryModel, id=pk)
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    services = Service.objects.all()
    countries = CountryModel.objects.all()
    
    if query:
        jobs = country.jobs.filter(title__icontains= query) 
    else:
        jobs = country.jobs.all() 
    for job in jobs:
            job.split_job_type = f"{job.job_type.split('_')[0]} {job.job_type.split('_')[1]}"

            
    context= {
        'country': country,
        'jobs':jobs,
        'contact':contact,
        'settings':settings,
        'services':services,
        'countries':countries
    }
    return render(request, 'country.html',context)



@require_http_methods(['GET'])
def countries(request):
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    services = Service.objects.all()
    countries = CountryModel.objects.all()

    return render(request, 'countries.html',{
        'contact':contact,
        'settings':settings,
        'services':services,
        'countries':countries
    })