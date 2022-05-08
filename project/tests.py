
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
<<<<<<< HEAD
       User.objects.create(username='aren', password='123123')
=======
       User.objects.create(username='arenn', password='123123')
>>>>>>> 90cb0527c28c6c80f47d5ec23bab46e6b809c71c
       self.client.login(username='username',password='password')
       response = self.client.get(reverse('logoutUser'), follow=True)
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context["user"].is_authenticated)

<<<<<<< HEAD

=======
>>>>>>> 90cb0527c28c6c80f47d5ec23bab46e6b809c71c
########################new test#####################




<<<<<<< HEAD

'''
# ------------tests for some admin functionality  ------     -- ------------------
#@tag("unit_test")
class PagehomeTests(TestCase):
=======
'''

# ------------tests for some admin functionality  ------     -- ------------------
#@tag("unit_test")

class pagehoameTests(TestCase):
>>>>>>> 90cb0527c28c6c80f47d5ec23bab46e6b809c71c
    @tag('unit-test')
    def test_ passegers_register(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
<<<<<<< HEAD
        self.assertTemplateUsed(response, 'signupasdesfaef')

=======
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
>>>>>>> 90cb0527c28c6c80f47d5ec23bab46e6b809c71c

'''
