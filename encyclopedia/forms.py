from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)

    from django.core.exceptions import ValidationError

    def validate_password_strength(value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
    
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class FarmForm(forms.Form):
    EQUIPMENT_CHOICES = [
        ('tractor', 'Tractor'),
        ('seeder', 'Seeder'),
        ('seed_drill', 'Seed Drill'),
        ('irrigation_system', 'Irrigation System'),
        ('harvester', 'Harvester'),
        ('fertilizer', 'Fertilizer'),
        ('spreader', 'Spreader'),
        ('pesticide_sprayer', 'Pesticide Sprayer'),
        ('plough', 'Plough'),
        ('cultivator', 'Cultivator'),
        ('aerial_applicator', 'Aerial Applicator'),
    ]

    SOIL_TYPE_CHOICES = [
        ('', '--- Select ---'),
        ('Desert Soil', 'Desert Soil'),
        ('Arctic Soil', 'Arctic Soil'),
        ('Tundra Soil', 'Tundra Soil'),
        ('Permafrost', 'Permafrost'),
        ('Taiga Soil', 'Taiga Soil'),
        ('Red Soil', 'Red Soil'),
        ('Brown Soil', 'Brown Soil'),
        ('Black Soil', 'Black Soil'),
        ('Rain forest Soil', 'Rain forest Soil'),
    ]

    location = forms.CharField(label='Location', max_length=100)
    farm_size = forms.FloatField(label='Farm Size')
    capital = forms.FloatField(label='Capital')
    soil_type = forms.ChoiceField(label='Soil Type', choices=SOIL_TYPE_CHOICES)
    equipment = forms.MultipleChoiceField(label='Equipment', choices=EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 5}), required=True)


