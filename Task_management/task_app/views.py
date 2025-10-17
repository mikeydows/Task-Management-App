from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .models import Task
from .forms import ProfileUpdateForm, TaskForm, UpdateEmailForm
from django.contrib.auth.decorators import login_required
import os

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

        if first_name is None:
            messages.error(request, "Enter your first name")
            return redirect('signup')

        elif last_name is None:
            messages.error(request, "Enter your last name")
            return redirect('signup')


        if password1 != password2:
            messages.error(request, "Passwords don’t match.")
            return redirect('signup')
        
        if email is None:
            messages.error(request, "Enter your email")
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

        if user is None:
            messages.error(request, "Wrong credentials, Try logging in")
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')
           
    return render(request, 'register/login.html')

def addtask(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST.get("title")
            tasks = request.POST.get("tasks")
            priority = request.POST.get("priority")
            Task.objects.create(user=request.user, title=title, tasks=tasks, priority = priority)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, "addtask.html")

def about(request):
    pass

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect("profile")
    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {"p_form": p_form}
    return render(request, "profile.html", context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, 'delete_task.html', {"task":task})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user = request.user)  # ✅ Fix: use Task (capital T)
    task.completed = True
    task.progress = 100
    task.save()
    return redirect('home')

def completed_task(request):
    completed = Task.objects.filter(user = request.user, completed=True)
    return render(request, 'completed_task.html', {'tasks': completed})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance = task)
    return render(request, "task_form.html", {"form": form, 'edit': True})

@login_required
def change_email(request):
    if request.method == "POST":
        new_email = request.POST.get('email')
        if new_email:
            request.user.email = new_email
            request.user.save()
            return redirect('profile')
    return render(request, 'change_email.html')


@login_required
def change_password(request):
    if request.method == "POST":
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if new_password == confirm_password:
            request.user.password = new_password
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
        else:
            messages.error(request, "Passwords do not match")
    return render(request, 'change_password.html')

@login_required
def remove_profile_picture(request):
    if request.user.profile.picture:
        picture_path = request.user.profile.picture.path
        if os.path.exists(picture_path):
            os.remove(picture_path)
        request.user.profile.picture = None
        request.user.profile.save()
    return redirect('profile')

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("home")
    return render(request, 'delete_account.html')
        