from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError  # Added to catch duplicate username errors
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required  # This ensures only authenticated users can access the profile page
def profile_view(request):
    # Get the profile for the logged-in user
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, "Username and password are required!")
            return redirect('register')

        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Username already exists. Try another one!")
            return redirect('register')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome !")
            return redirect('course_overview')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def course_overview(request):
    courses = [
        {'name': 'Python Basics', 'description': 'Learn Python from scratch', 'url': 'python_course'},
        {'name': 'Django Web Development', 'description': 'Build web applications using Django', 'url': 'web_dev'},
        {'name': 'Data Science', 'description': 'Analyze data using Python', 'url': 'data_science'},
        {'name': 'Cyber Security', 'description': 'Learn to secure networks and applications', 'url': 'cyber_security'},
    ]
    return render(request, 'course_overview.html', {'courses': courses})

def python_course(request):
    return render(request, 'python_course.html')

def web_dev(request):
    return render(request, 'web_dev.html')

def data_science(request):
    return render(request, 'data_science.html')

def cyber_security(request):
    return render(request, 'cyber_security.html')

def pyen(request):
    return render(request,'pyen.html')
def web(request):
    return render(request,'web.html')
def data(request):
    return render(request,'data.html')
def cyber(request):
    return render(request,'cyber.html')
def logout_view(request):
    logout(request)
    return redirect('home')


