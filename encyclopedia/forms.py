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

class FarmCalculatorForm(forms.Form):
    location = forms.CharField(max_length=100, required=True)
    size = forms.IntegerField(label="Farm Size (Acres)", min_value=0, required=True)
    capital = forms.IntegerField(label="Available Capital", min_value=0, required=True)
    equipment = forms.ChoiceField(choices=[
        ('', '--Select--'),
        ('tractor', 'Tractor'), 
        ('combine', 'Combine Harvester'),
        ('other', 'Other')
     ], required=True)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 5}), required=True)

from django import forms

class FarmCalculatorForm(forms.Form):
    location = forms.CharField(max_length=50, required=True)
    farm_size = forms.IntegerField(min_value=0, required=True)
    capital = forms.IntegerField(min_value=0, required=True)
    equipment = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=[
            ('tractor', 'Tractor'),
            ('seeder', 'Seeder'),
            # ... add all your equipment choices ...
        ]
    )
    soil_type = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Select a soil type'),  # Placeholder option
            ('Desert Soil', 'Desert Soil'),
            ('Arctic Soil', 'Arctic Soil'),
            # ... add all your soil type choices ...
        ]
    ) 
