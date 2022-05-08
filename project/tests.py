
from django.test import TestCase, tag
from django.urls import reverse
from project.models import *
##################################################################
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse
from django.test import Client
from App.models import *
import requests
  
  # Create your tests here.
class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='areen1', password='123123')
       self.client.login(username='username',password='password')
       response = self.client.get(reverse('logout'), follow=True)
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context["user"].is_authenticated)

class ManageUsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='email',
                                        last_name='last_name',
                                        first_name='first_name')
        self.user.set_password('password')
        self.user.save()
########################new test#####################






# ------------tests for some admin functionality  ------     -- ------------------
#@tag("unit_test")
class PagehomeTests(TestCase):
    @tag('unit-test')
    def test_ passegers_register(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signupasdesfaef')



