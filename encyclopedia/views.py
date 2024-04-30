from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .forms import NewUserForm, LoginForm, ContactForm, FarmForm
from django.http import JsonResponse
import requests
import openai
import random
from decimal import Decimal
import re

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
            return redirect('input')
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

def calculate_yield_cost(location, farm_size, capital, equipment, soil_type):
    estimated_yield_per_acre = estimate_yield(soil_type)
    estimated_cost_per_acre,estimated_yield_per_acre = estimate_cost(capital, equipment, farm_size,estimated_yield_per_acre)  
    total_yield = (estimated_yield_per_acre) * farm_size
    total_cost = estimated_cost_per_acre * farm_size
    return total_yield, total_cost
        
def estimate_yield(soil_type):
    yield_per_acre = 0
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
    return yield_per_acre
        # Add more conditions for other soil types
    '''
    a=random.randint(0,150)
    if a > 100:
        yield_per_acre *= random.uniform(0.7,0.9)  # Reduce yield by 20% in dry areas
    elif 50<a<100:
        yield_per_acre *= random.uniform(1.1,1.3) # Increase yield by 20% in wet areas
    elif a > 100:
            yield_per_acre *= random.uniform(0.7,0.9)
    return yield_per_acre
    '''

def estimate_cost(capital, equipments, farm_size, estimated_yield_per_acre):
    cost_per_acre = 500  # Example cost in dollars per acre
    if capital < 10000:
        cost_per_acre += 50  # Increase cost per acre for low capital
    elif capital > 50000:
        cost_per_acre -= 50  # Decrease cost per acre for high capital        
    if "tractor" in equipments:
        cost_per_acre += 100  # Increase cost per acre if tractor is available
        estimated_yield_per_acre *= random.uniform(1.17,1.26)  # Increase yield by 20% if tractor is available
    if "harvester" in equipments:
        cost_per_acre += 150
        estimated_yield_per_acre *= random.uniform(1.27,1.36)
    if "irrigation_system" in equipments:
        cost_per_acre += 200
        estimated_yield_per_acre *= random.uniform(1.36,1.47)
    if "plough" in equipments:
        cost_per_acre += 50
        estimated_yield_per_acre *= random.uniform(1.07,1.16)
    if "seed_drill" in equipments:
        cost_per_acre += 50
        estimated_yield_per_acre *= random.uniform(1.07,1.16)
    if "fertilizer_spreader" in equipments:
        cost_per_acre += 75
        estimated_yield_per_acre *= random.uniform(1.11,1.20)
    if "sprayer" in equipments:
        cost_per_acre += 50
        estimated_yield_per_acre *= random.uniform(1.07,1.16)
    if "cultivator" in equipments:
        cost_per_acre += 100
        estimated_yield_per_acre *= random.uniform(1.18,1.27)
    if "aerial_applicator" in equipments:
        cost_per_acre += 200
        estimated_yield_per_acre *= random.uniform(1.37,1.47)
    return cost_per_acre, estimated_yield_per_acre



def input_view(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            # Accessing form data
            location = form.cleaned_data['location']
            farm_size = form.cleaned_data['farm_size']
            capital = form.cleaned_data['capital']
            soil_type = form.cleaned_data['soil_type']
            equipment = form.cleaned_data['equipment']
            print(equipment)

            expected_yield, expected_cost = calculate_yield_cost(location, farm_size, capital, equipment, soil_type)
            
            # Store modified data in session
            profit_loss=expected_cost-capital
            txt=get_chatbot_suggestions(location, farm_size, expected_cost, equipment,soil_type,expected_cost)
            a=txt.split("Spring")
            fall_html=fall_parse(a[0])
            spring_html=spring_parse(a[1])
            request.session['form_data'] = {
                'expected_cost': expected_cost,
                'expected_yield': round(expected_yield,2),
                'fall_table': fall_html,
                'spring_table': spring_html,
            }
            return redirect('display')
    else:
        form = FarmForm()
    return render(request, 'encyclopedia/input.html', {'form': form})

def get_chatbot_suggestions(location, farm_size, profit_loss, equipment,soil_type,expected_cost):
    # Format the parameters into a question for the chatbot
    openai.api_key='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 '
    prompt = f"\nGive a list of the 5 best crops to grow in fall and 5 best crops for spring on the basis of "+ soil_type+" type, and "+ location +" as location. Also, give the monetary value of total produce possible on "+str(farm_size)+" acres of land. For the monetary value just multiply acres of land and then optimize according to crop costs and do it differently for each crop the amount should ideally be greater than the"+str(expected_cost)+".Also add a third column expeted profit which should be this monetary value - "+str(expected_cost)+". The output should be of the form 'Fall Crops: 1. crop name - $revenue $profit,2...   when fall crops are finished leave 4 blank spaces and then same for spring crops.  Don't explain, just say the crop and money amount"

    # Use the OpenAI API to get a response
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the assistant's message from the response
    assistant_message = response['choices'][0]['message']['content']

    return assistant_message

def display_view(request):
    form_data = request.session.get('form_data')

    return render(request, 'encyclopedia/display.html', {'form_data': form_data})


def fall_parse(data):
    a=data[11:]
    return a

def spring_parse(data):
    a=data[7:]
    return a