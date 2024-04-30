from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path('signup/', views.signup_view, name='signup'),
    path('gpts/', views.chatbot, name='chatbot'),
    path('services/', views.services, name='services'),
    path('details/', views.details, name='details'),
    path('contacts/', views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('input/', views.input_view, name='input'),
    path('display/', views.display_view, name='display'),
]
