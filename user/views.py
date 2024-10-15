from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import UserProfile
from .forms import EmailLoginForm
from home.models import Contact, Setting
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def register(request):
    contact = Contact.objects.get(id=1)
    settings = Setting.objects.get(id=1) 
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the user
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['email'],  # Set email as username
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['name']
                user.save()

                # Create the user profile
                profile = UserProfile(
                    name=form.cleaned_data['name'],
                    user=user,
                    phone_number=form.cleaned_data['phone_number'],
                    country=form.cleaned_data['country'],
                    city=form.cleaned_data['city'],
                    zip_code=form.cleaned_data['zip_code'],
                    job_title=form.cleaned_data['job_title'],
                    skill=form.cleaned_data['skill'],
                    expected_salary=form.cleaned_data['expected_salary'],
                    resume=form.cleaned_data['resume'],
                )
                profile.save()

                # Automatically log in the user
                login(request, user)
                return redirect('careers_job_list')  # Redirect to home page after registration
            except IntegrityError as e:
                form.add_error(None, 'A user with this email already exists.')
                print(e)
        
        print(form.errors.as_json())    
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form,
    'contact':contact,
    'settings':settings,
    })


def email_login_view(request):
    settings = Setting.objects.get(id=1)
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Username is the email here
            if user is not None:
                login(request, user)
                return redirect('careers_job_list')  # Redirect to home page or desired page
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = EmailLoginForm()

    return render(request, 'login.html', {'form': form, 'settings':settings})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    # Get the user profile or create it if it doesn't exist
    profile = UserProfile.objects.get(user=user)
    
    return render(request, 'profile.html',
    {'user': user, 'profile': profile}
    )



