from unicodedata import name
import django
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name="index"),
    path('abouthome',views.abouthome,name="abouthome"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('Login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('DriverSignup/',views.DriverSignup,name="DriverSignup"),
    path('AdminHomePage/',views.AdminHomePage,name="AdminHomePage"),
    path('AddNewDriver/',views.AddNewDriver,name="AddNewDriver"),
    path('PassengerHomePage/',views.PassengerHomePage,name="PassengerHomePage"),
    path('SendMail/',views.SendMail,name="SendMail"),
    path('map/',views.tripinfo,name="tripinfo"),
    path('PassengerGetDic/',views.PassengerGetDic,name="PassengerGetDic"),
   



]