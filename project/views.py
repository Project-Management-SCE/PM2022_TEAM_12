from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
import googlemaps
from datetime import datetime
from django.shortcuts import redirect

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
def login(request):
    return render(request,'project/login.html')
def PassengerGetDic(request):
    return render(request,'project/PassengerGetDic.html')
def signup(request):
    return render(request,'project/signup.html')
def DriverSignup(request):
    return render(request,'project/DriverSignup.html')
def AdminHomePage(request):
    return render(request,'project/AdminHomePage.html')
def AddNewDriver(request):
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


def tripinfo(request):
    k=Busway(request.session['fromm'],request.session['tooo'])
    return render(request,'project/PassengerGetDic.html',{'busnum':k[0],'buscompany':k[2],'busstation':k[1],'fromm':request.session['fromm'],'too':request.session['tooo']})  







def SendMail(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message = '''
        New message: {}

        Frome:{}

        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message ,'',['scegotrip@gmail.com'])

    return render(request,'project/SendMail.html')
