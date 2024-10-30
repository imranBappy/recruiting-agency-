from django.db import models
from country.models import Country
from utils.validator import  validate_file_size
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from job.position import positions
 

class Job(models.Model):
    title = models.CharField(max_length= 250)
    posted=models.DateField(auto_created=True, auto_now_add=True)
    JOB_TYPE_CHOOSE = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("remote", "Remote"),
    ]
    job_type = models.CharField(choices=JOB_TYPE_CHOOSE,max_length=250, default="full_time")
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    zip_code=models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='jobs')
    description=models.TextField(max_length=5000)
    
    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.CharField(max_length=15)
    skills = models.TextField(max_length=450)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply_job')
    resume = models.FileField(upload_to='resumes/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size],
    blank=True,  # Allow form submission without resume
    null=True    # Store null in the database if no file is provide
    ) 
    coverLetter = models.FileField(upload_to='coverLetters/',validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size],
    blank=True,  # Allow form submission without resume
    null=True    # Store null in the database if no file is provide
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications',blank=True ,  null=True  )

    def __str__(self):
        return self.name

class Client(models.Model):
    first = models.CharField(max_length=250)
    last = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250,blank=True, null=True )
    companyName = models.CharField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)
    # resume = models.FileField(upload_to='resumes/',
    # validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size],
    # blank=True, null=True 
    # )
    comment = models.TextField(max_length=5000,blank=True, null=True)


class CurrentLocation(models.Model):
    location = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.id} - {self.location}"

class Candidate(models.Model):
    agreed = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, blank=True, null=True)
    whatsApp = models.CharField(max_length=250)
    email = models.EmailField(max_length=250,blank=True, null=True )
    exp2 = models.CharField(max_length=250,blank=True, null=True)
    exp = models.CharField(max_length=250,blank=True, null=True)

    
    CATEGORY = {
        'CIVIL':"Civil",
        'MECHANICAL':"Mechanical",
        'ELECTRIAL':"Electrial",
        'IT':"It",
        'INSTRUMENTATION':"Instrumentation",
        'ADMIN':"Admin/HR",
        'SAFETY':"Safety",
        'STAFF':"Project/Planning/Staff",
        'DESIGN':"Design",
        'HEALTHCARE':"Healthcare",
        'HOSPITALITY':"Hospitality",
        'SECURITY':"Security",
        'LOGISTICS':"Logistics",
        'OPERATORS':"Operators/Drivers",
        'OTHER':"Other",
    }
    
    category = models.CharField( choices=CATEGORY, default='OTHER', max_length=250,  blank=True, null=True)
    JOB_POSITION = positions
   
    position = models.CharField(choices=JOB_POSITION, max_length=250)
    location = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='candition_location',  blank=True, null=True)
    currentLocation =  models.ForeignKey(CurrentLocation, on_delete=models.CASCADE, related_name='candition_CurrentLocation',  blank=True, null=True)
    resume = models.FileField(upload_to='resumes/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size],
    blank=True, null=True 
    )
    def __str__(self):
            return self.name

class Employee(models.Model):
    name = models.CharField(max_length=250)    
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, )
    companyName = models.CharField(max_length=250)   
    position = models.CharField(max_length=250)    
    requirement = models.TextField(max_length=250) 
    def __str__(self):
                return self.name


class Study(models.Model):
    firstName = models.CharField(max_length=250)   
    lastName = models.CharField(max_length=250)    
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    age = models.CharField(max_length=100)
    location = models.CharField(max_length=250)   
    IELTS_CHOICES = [
        ('YES','Yes'),
        ('NO','No'),
    ]
    position = models.CharField(max_length=250)   
    ielts = models.CharField(max_length=100, choices=IELTS_CHOICES)
    def __str__(self):
                return self.name


class Grievance(models.Model):
    name = models.CharField(max_length=250)    
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=250)   
    remarks  = models.TextField(max_length=250)   
    def __str__(self):
                return self.name



class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_user')
    job =  models.ForeignKey(Job, on_delete=models.CASCADE, related_name='jobs_save')