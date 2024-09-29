from django.db import models
from django.db import migrations
from utils.validator import  validate_file_size
from django.core.validators import FileExtensionValidator

# Create your models here.

class Slider(models.Model):
    img = models.FileField(upload_to='general/',   validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    def __str__(self):
        return self.title

class Award(models.Model):
    img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Video(models.Model):
    url = models.URLField(max_length=300)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title




class Serve(models.Model):
    img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg']), validate_file_size])
    title = models.CharField(max_length=100)
    banner = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    details_title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    side_Img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    def __str__(self):
        return self.title



class Service(models.Model):
    icon = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    banner = models.FileField(upload_to='general/',
     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size]
    )
    details = models.CharField(max_length=1000)
    side_Img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    def __str__(self):
        return self.title


class CadidateRegistion(models.Model):
    whatsApp=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Contact(models.Model):
    phone=models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    whatsApp=models.CharField(max_length=15)
    fb = models.URLField()
    x = models.URLField()
    linkedin = models.URLField()
    youtube = models.URLField()
    whatsAppLink = models.URLField()
    location = models.TextField(max_length=250)
    qr_code = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    def __str__(self):
        return self.email


class Setting(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    logo = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    def __str__(self):
        return self.title



