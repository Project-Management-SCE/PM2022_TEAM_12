import unittest
from multiprocessing.dummy.connection import Client
from .models import Driver
import django
from django.test import TestCase, tag
from django import setup
from django.test import TestCase, tag
from django.urls import reverse
from track.models import *
  
class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='areen', password='123123')
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
