from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('abme',views.abme, name='abme'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('services/moredetails',views.moredetails, name='services/moredetails'),
    # path('services/login',views.login, name='services/login'),
]