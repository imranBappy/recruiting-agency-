from django.db import models
from django.utils import timezone
from utils.validator import  validate_file_size
from django.core.validators import FileExtensionValidator

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=250)
    banner = models.FileField(upload_to='general/',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_file_size] )
    flag = models.FileField(upload_to='general/',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','svg']), validate_file_size] )
    created = models.DateTimeField(default=timezone.now)
    
    CONTINENT_CHOOSE = [
        ("asia", "Asia"),
        ("europe", "Europe"),
        ("middle_east", "Middle East"),
    ]
    continent = models.CharField(choices=CONTINENT_CHOOSE, max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

