import unittest
from multiprocessing.dummy.connection import Client
from .models import Driver
import django
from django.test import TestCase, tag
from django import setup


class LogTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(LogTest, cls).setUpClass()
            django.setup()

    @tag('unit-test')
    def test_login(self):
        login=self.client.login(username='soso', password='S263safa')
        self.assertFalse(login)
        
'''
class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='israa1', password='123')
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
        self.user.save()'''