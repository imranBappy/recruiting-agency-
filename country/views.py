from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Country

# Create your views here.


def country(request, pk):
    query = request.GET.get("job_search","")
    country = get_object_or_404(Country, id=pk)
    
    if query:
        jobs = country.jobs.filter(title__icontains= query) 
    else:
        jobs = country.jobs.all() 
    

    context= {
        'country': country,
        'jobs':jobs,
        'countries' :  Country.objects.all(),
    }
    template = loader.get_template("country.html")
    return HttpResponse(template.render(context))
