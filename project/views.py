from unicodedata import name
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as LL
from project.models import User,Driver
from django.views.decorators.csrf import csrf_exempt
from . forms import MyfileuploadForm
import smtplib


# Create your views here.
def index(request):
    return render(request,'index.html')

def abouthome(request):
    return HttpResponse("Home page")

def add(request,a,b):
    return HttpResponse(a+b)
def myfirstpage(request):
    return render(request,'index.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username=request.POST.get('name')
        pass1=request.POST.get('password')
        user = authenticate(username=username,password=pass1)
        if user is not None:
            LL(request, user)
            if user.is_authenticated and user.is_passenger :
                return redirect('PassengerHomePage') #Go to student home
            elif Driver.objects.filter(username=user.username):
                return redirect('DriverHomePage') #Go to teacher home
            elif user.is_authenticated and user.is_Admin==True :
                return redirect('AdminHomePage') #Go to teacher home
        else:
            messages.error(request,pass1)
            # Invalid email or password. Handle as you wish
            return redirect('login')

    return render(request,'project/login.html')

def DriverSignup(request):

    if request.method == "POST":
        email=request.POST.get('Demail')
        fname=request.POST.get('DFname')
        lname=request.POST.get('DLname')
        companyName=request.POST.get('companyname')
        phone=request.POST.get('Dhone')
        myuser=Driver.objects.create_user(username=fname+" "+lname,password="1111")
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.companyName=companyName
        myuser.phone=phone
        myuser.save()
        messages.success(request,"succseful")
        LL(request, myuser)

        return redirect('DriverFile')
    return render(request,'project/DriverSignup.html')


@csrf_exempt
def DriverFile(request):
    context = {
        'form':MyfileuploadForm()
    }

    if request.method == 'POST':
        driver=Driver(request.POST,request.FILES)
        if driver is not None:
            myuser=Driver.objects.get(username=request.user.username)
            license=request.FILES.get('License')
            Certificate=request.FILES.get('certificate')
            myuser.certificate=Certificate      
            myuser.License=license
            myuser.save()
            return redirect('login')
    return render(request,'project/DriverFile.html',context)

def DriverHomePage(request):
     return render(request,'project/DriverHomePage.html')

