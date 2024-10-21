from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Slider, Award, Video, Serve, Contact, Setting, Service
from country.models import Country

# Create your views here.

def index(request):
    sliders = Slider.objects.all()
    awards = Award.objects.all()
    videos = Video.objects.all()
    serves = Serve.objects.all()
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    context = {
        'sliders':sliders,
        'awards':awards,
        'videos': videos,
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
        'serves':serves
    }
   
    return render(request, 'home2.html', context)




def service(request, pk):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    service = Service.objects.get(id=pk)
    
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
        'service':service
    }

    return render(request, 'service.html', context )

def serve(request, pk):
    services = Service.objects.all()
    countries = Country.objects.all()
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    serve = Serve.objects.get(id=pk)
    
    context = {
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings,
        'serve':serve
    }

    return render(request, 'serve.html', context )




def about(request):
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

    return render(request, 'about.html', context )

def survey(request):
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1)
    countries = Country.objects.all()

    context = {
        'contact':contact,
        'settings':settings,
        'countries':countries,

    }
    return render(request, "survey.html",context)