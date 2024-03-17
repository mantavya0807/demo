from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .forms import NewUserForm, LoginForm, FarmCalculatorForm, ContactForm
from django.http import JsonResponse
import requests
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('details')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'Encyclopedia/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'Encyclopedia/logout.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login_view')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'Encyclopedia/signup.html')

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
    return render(request, 'core/main.html')

def services(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
    return render(request, 'encyclopedia/services.html')

def details(request):
    if request.method == 'POST':
        form = FarmCalculatorForm(request.POST)
        if form.is_valid():
            result = calculate_yield_cost(request)
            return render(request, 'encyclopedia/result.html', {'form': form, 'result': result})
    else:
        form = FarmCalculatorForm()
    return render(request, 'encyclopedia/details.html', {'form': form})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        pass  # Process the form data
    return render(request, 'encyclopedia/contacts.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.") 
    return redirect('index')

def calculate_yield_cost(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        farm_size = request.POST.get('size')
        capital = request.POST.get('capital')
        equipment = request.POST.getlist('equipment')  # Get a list of selected equipment
        soil_type = request.POST.get('soil_type')

        estimated_yield_per_acre = estimate_yield(request)
        estimated_cost_per_acre = estimate_cost(request)
        
        total_yield = estimated_yield_per_acre * 13
        total_cost = estimated_cost_per_acre * 13
        
        return total_yield, total_cost
    else:
        return None, None
        
def estimate_yield(request):
    if request.method == 'POST':    
        yield_per_acre = 0
        soil_type = request.POST.get('soil_type')
        # Example: Estimate yield based on soil type
        if soil_type == "Desert Soil":
            yield_per_acre =  random.randint(2,4)  # Example yield in units per acre
        elif soil_type == "Arctic Soil":
            yield_per_acre = random.randint(3,5)
        elif soil_type == "Tundra Soil":
            yield_per_acre = random.randint(3,5)
        elif soil_type == "Permafrost":
            yield_per_acre = random.randint(4,6)
        elif soil_type == "Taiga Soil":
            yield_per_acre = random.randint(5,7)
        elif soil_type == "Red Soil":
            yield_per_acre = random.randint(6,8)
        elif soil_type == "Brown Soil":
            yield_per_acre = random.randint(7,9)
        elif soil_type == "Black Soil":
            yield_per_acre = random.randint(11,13)
        elif soil_type == "Rain forest Soil":
            yield_per_acre = random.randint(12,14)
        
        # Add more conditions for other soil types
        a=random.randint(0,150)
        if a > 100:
            yield_per_acre *= random.uniform(0.7,0.9)  # Reduce yield by 20% in dry areas
        elif 50<a<100:
            yield_per_acre *= random.uniform(1.1,1.3) # Increase yield by 20% in wet areas
        elif a > 100:
            yield_per_acre *= random.uniform(0.7,0.9)
        return yield_per_acre
    else:
        return 10

def estimate_cost(request):
    if request.method == 'POST':
        capital = request.POST.get('capital')
        equipments = request.POST.getlist('equipment')
        soil_type = request.POST.get('soil_type')

        cost_per_acre = 500  # Example cost in dollars per acre
        
        if capital < 10000:
            cost_per_acre += 50  # Increase cost per acre for low capital
        elif capital > 50000:
            cost_per_acre -= 50  # Decrease cost per acre for high capital
        
        if "Tractor" in equipments:
            cost_per_acre += 100  # Increase cost per acre if tractor is available
        # Add more conditions for other equipment
        
        return cost_per_acre
    else:
        return 'elo'

def result(request):  # Renamed function for clarity
    form = FarmCalculatorForm(request.POST or None)
    if form.is_valid():
        # Access cleaned data
        location = form.cleaned_data['location']
        farm_size = form.cleaned_data['size']
        capital = form.cleaned_data['capital']
        equipment = form.cleaned_data['equipment']  # List of selected equipment
        soil_type = form.cleaned_data['soil_type']

        # Perform calculations
        estimated_yield = estimate_yield(location, soil_type, farm_size, equipment)
        estimated_cost = estimate_cost(capital, equipment, farm_size)

        # Prepare data for the results page
        result = f"Estimated Yield: {estimated_yield}, Estimated Cost: {estimated_cost}"

        context = {
            'location': location,
            'equipment': equipment,
            'farm_size': farm_size,
            'result': result
        }

        return render(request, 'result.html', context) 
    else:
        # If form is not valid, re-render the form page 
        return render(request, 'encyclopedia/details.html', {'form': form})
    return render(request, 'encyclopedia/result.html', {'form': form})

def post(request):
    form = FarmCalculatorForm(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data['class FarmCalculatorForm']
    args = {'form': form, 'text': text}
    return render(request, 'encyclopedia/details.html', args)
