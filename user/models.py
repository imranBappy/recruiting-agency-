from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # Changed to OneToOneField
    name= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    skill = models.CharField(max_length=200)
    expected_salary = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/')
    img = models.FileField(upload_to='general/')

    def __str__(self):
        return f"{self.id} - {self.name}"
