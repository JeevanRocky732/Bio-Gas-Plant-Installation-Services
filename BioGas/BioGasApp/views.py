from email.utils import decode_rfc2231
from django.shortcuts import render
from datetime import datetime
from BioGasApp.models import Contact,Services
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def abme(request):
    return render(request,'abme.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def services(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        address = request.POST.get('address')
        services = Services(name=name, email=email, password=password, number=number,address=address, date = datetime.today())
        services.save()
        messages.success(request, 'You Succesfully Registred For Service')
    return render(request,'services.html')

def moredetails(request):
    return render(request,'moredetails.html')

# def login(request):
    # return render(request,'login.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(USERNAME=username, PASSWORD=password)