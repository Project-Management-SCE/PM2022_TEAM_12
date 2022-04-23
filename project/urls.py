from unicodedata import name
import django
from django.urls import path
from . import views
from . forms import MyfileuploadForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
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
    path('DriverFile/',views.DriverFile,name="DriverFile"),
    path('DriverHomePage/',views.DriverHomePage,name="DriverHomePage"),
    path('Request/',views.Request,name="Request"),
    path('<int:id>', views.details,name='detail'),
    path('<int:id>/"',views.accept,name="Accept"),
    path('<int:id>//',views.decline,name="Decline"),
     path('map/',views.tripinfo,name="tripinfo"),
    path('PassengerGetDic/',views.PassengerGetDic,name="PassengerGetDic"),
     path('DriverDetails/',views.DriverDetails,name="DriverDetails"),
     path('deluser/',views.deluser,name="deluser"),
     path('delete/<int:id>',views.delete,name="delete"),
    path('deleteDriver/<int:id>',views.deleteDriver,name="deleteDriver"),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)