from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Slider, Award, Video, Service, Contact, Setting
from country.models import Country

# Create your views here.

def index(request):
    
    sliders = Slider.objects.all()
    awards = Award.objects.all()
    videos = Video.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.get(id=1)
    countries = Country.objects.all()
    settings = Setting.objects.get(id=1)
    

    context = {
        'sliders':sliders,
        'awards':awards,
        'videos': videos,
        'services':services,
        'countries':countries,
        'contact':contact,
        'settings':settings
    }

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context))

