import django
from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse,resolve
from .models import *
from .views import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

'''
class ViewTest(TestCase):
    def test_login(self):
        self.client.login(username='areen', password='123123')
        response = self.client.get('/Login/')
        self.assertContains(response, 'login', 4, 200)
class medelsTest(TestCase):
    def test_create_message(self):
        message1=Updates.objects.create(message="title for messs",senderID="areen")
        message1.save()
        self.assertEqual(str(message1),"title for messs")

'''
class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='aren', password='123123')
       self.client.login(username='username',password='password')
       response = self.client.get(reverse('logoutUser'), follow=True)
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context["user"].is_authenticated)
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
        response = c.get(reverse('PassengerHomePage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'PassengerHomePage.html')

    def test_DriverNotification(self):
        c = Client()
        response = c.get(reverse('DriverNotification'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'DriverNotification.html')  

    def test_AddNewDriver1(self):
       c = Client()
       response = c.get(reverse('AddNewDriver'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver.html')  


    def test_AddNewDriver2(self):
       c = Client()
       response = c.get(reverse('AddNewDriver'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/SendMail.html') 

    def test_AddNewDriver3(self):
       c = Client()
       response = c.get(reverse('AddNewDriver'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/DriverDetails.html')   

    def test_AddNewDriver4(self):
       c = Client()
       response = c.get(reverse('AddNewDriver'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/deluser.html') 

    def test_AddNewDriver5(self):
       c = Client()
       response = c.get(reverse('AddNewDriver'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/Raquest.html')          


    def test_PageHome1(self):
       c = Client()
       response = c.get(reverse('index'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/signup.html') 

    def test_PageHome2(self):
       c = Client()
       response = c.get(reverse('index'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/login.html')        

    def test_PageHome3(self):
       c = Client()
       response = c.get(reverse('index'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/DriverSignup.html')

    def test_AdminHomePage1(self):
       c = Client()
       response = c.get(reverse('AdminHomePage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage.html')  

    def test_AdminHomePage2(self):
       c = Client()
       response = c.get(reverse('AdminHomePage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/SendMail.html')   

    def test_AdminHomePage3(self):
       c = Client()
       response = c.get(reverse('AdminHomePage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/AddNewDriver.html')  

    def test_AdminHomePage4(self):
       c = Client()
       response = c.get(reverse('AdminHomePage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/DriverDetails.html')  

    def test_AdminHomePage5(self):
       c = Client()
       response = c.get(reverse('AdminHomePage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/deluser.html')                       
