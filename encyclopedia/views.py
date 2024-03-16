from django.shortcuts import render, redirect
import markdown2
from . import util
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Path: encyclopedia/views.py


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle the form submission here
            pass
    else:
        form = LoginForm()

    return render(request, 'encyclopedia/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'encyclopedia/signup.html', {'form': form})
    
def home(request):
    respose= request.get()