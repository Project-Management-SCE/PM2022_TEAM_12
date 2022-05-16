#from unicodedata import name
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from email.message import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as LL
from project.models import User,Driver,Updates,Report
from project.forms import contactformemail
from datetime import datetime
import googlemaps
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . forms import MyfileuploadForm
import smtplib
keyy='AIzaSyAsUJ0P3eueaI2IdbInU6P4I6amqPyYHUI'
gmaps = googlemaps.Client(key=keyy)

# Request directions via public transit

def Busway(fromm,to):
     now = datetime.now()
     directions_result = gmaps.directions(fromm,to,mode="transit",departure_time=now)
     bus_num=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['short_name']
     bus_stations=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['name']
     bus_company=directions_result[0]['legs'][0]['steps'][0]['transit_details']['line']['agencies'][0]['name']
     return [bus_num,bus_stations,bus_company]


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
        name=request.POST['name']
        pass1=request.POST['password']
        myuser = authenticate(request,username=name,password=pass1)
        if myuser is not None:
            LL(request, myuser)
            if myuser.is_authenticated and myuser.is_passenger==True :
                return redirect('PassengerHomePage') #Go to student home
            elif Driver.objects.filter(username=myuser.username):
                return redirect('DriverHomePage') #Go to  home
            elif myuser.is_authenticated and myuser.is_Admin==True :
                return redirect('AdminHomePage') #Go to  home
        else:
            messages.error(request,"Invalid email or password")
            return redirect('login')
    return render(request,'project/login.html')



def signup(request):

    if request.method == "POST" :
        name=request.POST['username']
        pass1=request.POST['pass1']
        email=request.POST['email']
        fname=request.POST.get('Fname')
        lname=request.POST.get('Lname')
        myuser=User.objects.create_user(name,email,pass1)
        myuser.first_name=fname
        myuser.email=email
        myuser.last_name=lname
        myuser.is_passenger=True
        myuser.save()
        messages.success(request,"succseful")
        LL(request, myuser)
        return redirect('login')

    messages.error(request,"not added")
    return render(request,'project/signup.html')

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

def AdminHomePage(request):
    return render(request,'project/AdminHomePage.html')

def AdminReports(request):
    reports=Report.objects.all()
    return render(request,'project/AdminReports.html',{'users':reports})

def AddNewDriver(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('pass')
        myuser=Driver.objects.create_user(username=name,password=password)
        myuser.its_ok=False
        myuser.save()
        messages.success(request,"succseful")
        return redirect('AdminHomePage')
    return render(request,'project/AddNewDriver.html')  

def PassengerHomePage(request):
    if  request.method=='POST':

        fromm=request.POST.get('fromm')
        too=request.POST.get('tooo')
        request.session['fromm'] = fromm
        request.session['tooo'] = too
        print("***************************************\n\n\n")
        print(request.session['fromm'],request.session['tooo'] ) 
        print("***************************************\n\n\n")
        print(fromm,too) 
        print("***************************************\n\n\n")
        return redirect('/map')
    print(request.POST.get('fromm'),request.POST.get('too')) 
    print("***************************************")

    return render(request,'project/PassengerHomePage.html')
def PassengerGetDic(request):
    return render(request,'project/PassengerGetDic.html')

def PassengerProfile(request,id):
    user=get_object_or_404(User,id=id)
    return render(request,'project/PassengerProfile.html',{'user':user})
def PassengerPassword(request,id):
    user=get_object_or_404(User,id=id)

    if request.method=="POST":
        old_pass=request.POST.get('full_name')
        new_pass=request.POST.get('email')
        cpass=request.POST.get('confirmPassword')
        user1 = authenticate(username=user.username,password=old_pass)
        if user1 is not None and new_pass==cpass:
            user1.set_password(new_pass)
            user1.save()
            return render(request,'project/PassengerHomePage.html',{'user':user})
    return render(request,'project/PassengerPassword.html',{'user':user})




def tripinfo(request):
    k=Busway(request.session['fromm'],request.session['tooo'])
    return render(request,'project/PassengerGetDic.html',{'busnum':k[0],'buscompany':k[2],'busstation':k[1],'fromm':request.session['fromm'],'too':request.session['tooo']})  


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

def Request(request):
    userList= Driver.objects.filter(is_ok=False)
    return render(request, 'project/Request.html', {'users': userList})

def PMyTrip(request):
     return render(request,'project/PMyTrip.html')



def DriverDetails(request):
    user= Driver.objects.filter(is_ok=True)
    return render(request,'project/DriverDetails.html',{'users': user})

def details(request,id):
    user=get_object_or_404(Driver,id=id)
    return render(request,'project/detail.html',{'user':user})

def accept(request,id):
    user=get_object_or_404(Driver,id=id)
    user.is_ok=True
    user.save()
    return redirect('AdminHomePage')    

def decline(request,id):
    obj=get_object_or_404(Driver,id=id)
    obj.delete()
    return redirect('AdminHomePage')    

def logout_user(request):
    logout(request)
    return redirect('login')

def SendMail(request):
    if request.method=="POST":
        full_name = request.POST['full_name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
        subject,
        message,
        'from@emample.com',
        [email],
        fail_silently=False,        
        ) 
        return redirect('AdminHomePage')    

    return render(request,'project/SendMail.html')

def  deluser(request):
    user= User.objects.filter(is_passenger=True)
    return render(request,'project/deluser.html',{'users': user})

def delete(request,id):
    obj=User.objects.get(id=id)
    obj.delete()
    return redirect('deluser')

def Block(request,id):
    obj=Report.objects.get(id=id)
    A=User.objects.filter(username=obj.UserName)
    A.delete()
    obj.delete()
    return redirect('AdminHomePage')





def deleteDriver(request,id):
    obj=get_object_or_404(Driver,id=id)
    obj.delete()
    return redirect('DriverDetails') 

def logoutUser(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def DriverNotification(request):
    if request.method == "POST":
        senderID=request.user.username
        message=request.POST.get('Notification')
        bussNum=request.POST.get('BusNum')
        A=Updates(senderID=senderID,BusLine=bussNum,message=message)
        A.save()
        return redirect('DriverHomePage')
    return render(request,'project/DriverNotification.html')

def NotificationByDriver(request):  
    return render(request,'project/NotificationByDriver.html')  

def PassengerNotification(request):
    if request.method == "POST":
        busline=request.POST.get('bus_line')
        user=Updates.objects.filter(BusLine=busline)
        return render(request,'project/NotificationByDriver.html',{'updates':user})
    return render(request,'project/PassengerNotification.html')

def DriverChangePassword(request):
    if request.method == "POST" :
        old_pass=request.POST.get('full_name')
        new_pass=request.POST.get('email')
    return render(request,'project/DriverChangePassword.html')



def OrderTrip(request):
    return render(request,'project/OrderTrip.html')
def MyDrive(request):
    return render(request,'project/MyDrive.html')