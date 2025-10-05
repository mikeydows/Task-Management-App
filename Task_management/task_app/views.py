from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Task

def home(request):
    tasks = []
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

def signupPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password1 != password2:
            messages.error(request, "Passwords don’t match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)  # auto login after signup
        return redirect('home')
        
    return render(request, 'register/signup.html')

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials, Try logging in")
            return redirect('login')
    return render(request, 'register/login.html')

def addtask(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST.get("title")
            tasks = request.POST.get("tasks")
            Task.objects.create(user=request.user, title=title, tasks=tasks)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, "addtask.html")

def about(request):
    pass

def logoutPage(request):
    logout(request)
    return redirect('home')