from django.db import models
from country.models import Country
from utils.validator import  validate_file_size
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length= 250)
    posted=models.DateField(auto_created=True, auto_now_add=True)
    JOB_TYPE_CHOOSE ={
        "full_time":"full_time",
        "part_time":"part_time",
        "remote":"remote",
    }
    job_type = models.CharField(choices=JOB_TYPE_CHOOSE,max_length=250, default="full_time")
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    experience = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    zip_code=models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='jobs')
    description=models.CharField(max_length=500)
    
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

    
class Candidate(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    whatsApp = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, )
  
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
    
    category = models.CharField( choices=CATEGORY, default='OTHER', max_length=250)
    JOB_POSITION = {
        'SOFTWARE ENGINEER': 'Software Engineer',
        'DATA SCIENTIST': 'Data Scientist',
        'PRODUCT MANAGER': 'Product Manager',
        'DIGITAL MARKETING MANAGER': 'Digital Marketing Manager',
        'CLOUD ENGINEER': 'Cloud Engineer',
        'CYBERSECURITY ANALYST': 'Cybersecurity Analyst',
        'UX/UI DESIGNER': 'UX/UI Designer',
        'AI/ML ENGINEER': 'AI/ML Engineer',
        'DEVOPS ENGINEER': 'DevOps Engineer',
        'BUSINESS ANALYST': 'Business Analyst'
    }
    position = models.CharField(choices=JOB_POSITION, max_length=250)
    location = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='candition_location')
    resume = models.FileField(upload_to='resumes/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf']), validate_file_size]
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
    name = models.CharField(max_length=250)    
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    age = models.CharField(max_length=100)
    location = models.CharField(max_length=250)   
    position = models.CharField(max_length=250)   
    ielts = models.BooleanField()
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
    job =  models.ForeignKey(Job, on_delete=models.CASCADE, related_name='save')