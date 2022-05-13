import django

from django.db import models
from django.test import TestCase,SimpleTestCase,Client,tag
from django.urls import resolve
from .models import *
from .views import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group 
import requests



'''
class ViewTest(TestCase):
    def test_login(self):
        self.client.login(username='areen', password='123123')
        response = self.client.get('/Login/')
        self.assertContains(response, 'login', 4, 404)
class medelsTest(TestCase):
    def test_create_message(self):
        message1=Updates.objects.create(message="title for messs",senderID="areen")
        message1.save()
        self.assertEqual(str(message1),"title for messs")

'''
class LogoutTest(TestCase):
   def testLogout(self):
       user=User.objects.create(username='aren', password='123123')
       self.client.login(username='username',password='password')
       response = self.client.get(('logoutUser'), follow=True)
       self.assertEqual(response.status_code, 404)

'''
class ManageUsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='email',
                                        last_name='last_name',
                                        first_name='first_name')
        self.user.set_password('password')
        self.user.save() '''


class PassengerHomePageTests(TestCase): 

    def test_PassengerHomePage(self):
        c = Client()
        response = c.get(('PassengerHomePage'))
        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'PassengerHomePage.html')

    def test_DriverNotification(self):
        c = Client()
        response = c.get(('DriverNotification'))
        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'DriverNotification.html')  

    def test_AddNewDriver1(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AddNewDriver.html')  


    def test_AddNewDriver2(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AddNewDriver/SendMail.html') 

    def test_AddNewDriver3(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AddNewDriver/DriverDetails.html')   

    def test_AddNewDriver4(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AddNewDriver/deluser.html') 

    def test_AddNewDriver5(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AddNewDriver/Request.html')          


    def test_PageHome1(self):
       c = Client()
       response = c.get(('index'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'index/signup.html') 

    def test_PageHome2(self):
       c = Client()
       response = c.get(('index'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'index/login.html')        

    def test_PageHome3(self):
       c = Client()
       response = c.get(('index'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'index/DriverSignup.html')

    def test_AdminHomePage1(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage.html')  

    def test_AdminHomePage2(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage/SendMail.html')   

    def test_AdminHomePage3(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage/AddNewDriver.html')  

    def test_AdminHomePage4(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage/DriverDetails.html')  

    def test_AdminHomePage5(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage/deluser.html')

    def test_AdminHomePage6(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'AdminHomePage/Request.html')

    def test_deluser(self):
       c = Client()
       response = c.get(('deluser'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'deluser.html') 

    def test_DriverDetails(self):
       c = Client()
       response = c.get(('DriverDetails'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'DriverDetails.html')

    def test_DriverFile1(self):
       c = Client()
       response = c.get(('DriverFile'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'DriverFile.html')

    def test_DriverHomePage(self):
       c = Client()
       response = c.get(('DriverHomePage'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'DriverHomePage.html') 

    def test_DriverNotification(self):
       c = Client()
       response = c.get(('DriverNotification'))
       self.assertEquals(response.status_code, 404)
       self.assertTemplateNotUsed(response, 'DriverNotification.html')
       
    def test_DriverSignup1(self):
      c = Client()
      response = c.get(('DriverSignup'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'DriverSignup.html') 

    def test_DriverSignup2(self):
      c = Client()
      response = c.get(('DriverSignup'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'DriverSignup/DriverFile.html')  

    def test_login1(self):
      c = Client()
      response = c.get(('login'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'login.html')

    def test_login2(self):
      c = Client()
      response = c.get(('login'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'login/AsminHomePade.html')

    def test_login3(self):
      c = Client()
      response = c.get(('login'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'login/PassengerHomePage.html')

    def test_login4(self):
      c = Client()
      response = c.get(('login'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'login/DriverHomePage.html')

    def test_NotificationByDriver(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'NotificationByDriver.html')

    def test_PassengerNotification(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/PassengerNotification.html')   


    def test_PassengerNotification_logout(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/login.html')

    def test_PassengerNotification_home_pagre(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/PassengerHomePage.html') 

    def test_SendMail(self):
     c = Client()
     response = c.get(('SendMail'))
     self.assertEquals(response.status_code, 404)
     self.assertTemplateNotUsed(response, 'SendMail.html')



    def test_Signup(self):
      c = Client()
      response = c.get(('signup'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'signup.html')

    '''
    def test_Requset(self):
      c = Client()
      response = c.get(('Requset'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'Requset.html')
    '''
    
    def test_PassengerNotification1(self):
      c = Client()
      response = c.get(('PassengerNotification'))
      self.assertEquals(response.status_code, 404)
      self.assertTemplateNotUsed(response, 'PassengerNotification.html')  

    

####################################integration-test########################
@tag('integration_test')
class testPassengerHomePage_integration_test_class(TestCase): 

   def testRegisterStudentAndLogin_new(self):
        #User.objects.create(username='aa', password='aa'
       data = {'username': 'a12', 'password': 'a12'}
       data_login=User.objects.create () #+ User.objects.create = ({'name':'Areen'})

       response = self.client.post(('login'), data=data, follow=True)

       self.assertEqual(response.status_code, 404)


       response = self.client.post(('PassengerHomePage/'), data=data, follow=True)


       self.assertTemplateNotUsed(response, 'PassengerHomePage.html')
   
