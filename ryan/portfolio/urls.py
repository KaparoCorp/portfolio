from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('hmu', views.hmu, name='hit_me_up'),
   
]