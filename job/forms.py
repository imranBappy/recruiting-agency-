from django import forms

from .models import ApplyJob,Candidate,Employee,Study, Grievance,Client



class ApplyJobForm(forms.ModelForm):

    class Meta:
        model = ApplyJob
        fields = ["name", "designation", "email", "phone", "age", "skills", "resume", "coverLetter"]
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'  
        # fields = ('name', 'phone', 'whatsApp', 'email', 'category', 'position', 'location', 'resume')
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'phone': forms.TextInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'whatsApp': forms.TextInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'email': forms.EmailInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'category': forms.Select(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'position': forms.Select(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'location': forms.Select(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        #     'resume': forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-1 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        # }

        

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  

    

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = '__all__' 

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = '__all__' 