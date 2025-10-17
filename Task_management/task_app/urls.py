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
    path('complete/<int:task_id>/', views.complete_task, name = 'complete_task'),
    path('completed/', views.completed_task, name="completed_task"),
    path('edit/<int:task_id>/',views.edit_task, name = "edit_task"),
    path('change_email/', views.change_email, name = 'change_email'),
    path('change_password/', views.change_password, name = "change_password"),
    path('delete_account/', views.delete_account, name = "delete_account"),
    path('remove_profile_picture/', views.remove_profile_picture, name = "remove_profile_picture"),
]