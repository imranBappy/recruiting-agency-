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
        return f"{self.id} - {self.title}"

class Award(models.Model):
    img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.title}"

class Video(models.Model):
    url = models.URLField(max_length=300)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.title}"




class Serve(models.Model):
    img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg']), validate_file_size])
    title = models.CharField(max_length=100)
    banner = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    details_title = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    side_Img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    carousel = models.TextField(max_length=2000)
    options = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.id} - {self.title}"



class Service(models.Model):
    icon = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    banner = models.FileField(upload_to='general/',
     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size]
    )


    details = models.TextField(max_length=2000)
    side_Img = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    
    details2 = models.TextField(null=True , blank=True, max_length=2000)
    side_Img2 = models.FileField(null=True , blank=True, upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    image = models.FileField(null=True , blank=True, upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])

    def __str__(self):
        return f"{self.id} - {self.title}"


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
        return f"{self.id} - {self.name}"


class Contact(models.Model):
    phone=models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    whatsApp=models.CharField(max_length=15)
    fb = models.URLField(max_length=300,default="#")
    fb_group = models.URLField(max_length=300,default="#")
    x = models.URLField(max_length=300,default="#")
    linkedin = models.URLField(max_length=300,default="#")
    youtube = models.URLField(max_length=300,default="#")
    whatsAppLink = models.URLField(max_length=300,default="#")
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



class Team(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1000)
    photo = models.FileField(upload_to='general/',validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size])
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.id} - {self.name}"