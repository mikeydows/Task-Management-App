from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('signup/', views.signupPage, name='signup'),
    path('about/', views.about, name = 'about'),
    path('addtask/', views.addtask, name = 'addtask'),
    path('profile/', views.profile, name = 'profile'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('completed/', views.completed, name = 'completed')
]