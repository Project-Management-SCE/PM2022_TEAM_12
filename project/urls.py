from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('abouthome',views.abouthome,name="abouthome"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('Login/',views.login,name="login"),
    path('DriverSignup/',views.DriverSignup,name="DriverSignup"),    
    path('DriverFile/',views.DriverFile,name="DriverFile"),
    path('DriverHomePage/',views.DriverHomePage,name="DriverHomePage"),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)