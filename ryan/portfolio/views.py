from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# from .models import Item, Appraisal, Exchange, Rating, Category, CustomUser, ActivityLog, Notification, Message
# from .forms import ProfileForm, RegistrationForm
# from .forms import ItemForm, AppraisalForm, ExchangeForm, RatingForm, CategoryForm


# Create your views here.
# base view
def base(request):
    return render(request, 'base.html', {'user': request.user})

# home view
def home(request):
    return render(request, 'home.html', {'user': request.user})

# projects view
def projects(request):
    return render(request, 'projects.html', {'user': request.user})

# about view
def about(request):
    return render(request, 'about.html', {'user': request.user})

# hmu view [ hit me up ]
def hmu(request):
    return render(request, 'hmu.html', {'user': request.user})




