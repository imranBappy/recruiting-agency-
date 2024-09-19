from django.contrib import admin
from .models import Slider, Award, Video, Service, CadidateRegistion, Contact, Setting

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
  pass

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
  pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  pass

@admin.register(CadidateRegistion)
class CadidateRegistionAdmin(admin.ModelAdmin):
  pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  pass

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
  pass


