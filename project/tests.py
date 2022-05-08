
from django.test import TestCase, tag
from django.urls import reverse
from project.models import *
##################################################################
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse
from django.test import Client
from .models import *
import requests
  

  # Create your tests here.
class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='arenn', password='123123')
       self.client.login(username='username',password='password')
       response = self.client.get(reverse('logoutUser'), follow=True)
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context["user"].is_authenticated)

########################new test#####################




'''

# ------------tests for some admin functionality  ------     -- ------------------
#@tag("unit_test")

class pagehoameTests(TestCase):
    @tag('unit-test')
    def test_Add_Message_GET(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup')
    @tag('unit-test')
    def test_Add_Message_GET2(self):
        c = Client()
        response = c.get(reverse('createmessage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'teacher_templates/message_form.html')

    @tag('unit-test')
    def test_Add_Teacher_Message_GET(self):
        c = Client()
        response = c.get(reverse('create_teacher_message'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_templates/message_form.html')
        
'''

