from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Full Name',
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={
            'class':'w-full'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'w-full'
        })
    )
    confirm_password = forms.CharField( label="Re-enter Password",
        widget=forms.PasswordInput(attrs={
            'class':'w-full'
        })
    )
    phone_number = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    country = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    city = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    zip_code = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    job_title = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    skill = forms.CharField(max_length=200, help_text='List your skills separated by commas.',
        widget=forms.TextInput(attrs={
            'class':'w-full'
        })
    )
    expected_salary = forms.DecimalField(max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class':'w-full'
        })
    )
    resume = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        widget=forms.FileInput(attrs={
            'class':'w-full'
        })
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    # Validation for password match
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match!")
        return confirm_password

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume and resume.size > 5*1024*1024:  # 5MB limit
            raise ValidationError("Resume file is too large. Max size is 5MB.")
        return resume


class EmailLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full',
        'placeholder': 'Password'
    }))