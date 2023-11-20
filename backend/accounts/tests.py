
from django.contrib.auth.models import User
from django.core import mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class AccountsTestCase(APITestCase):

    def test_create_user(self):
        
        self.assertEqual(Token.objects.all().count(), 0)
        
        params = {
            "username": "piotr",
            "email": "piotr@example.com",
            "password": "verysecret",
        }
        user = User.objects.create_user(
            username=params["username"],
            email=params["email"],
            password=params["password"],
        )
        token = Token.objects.create(user=user)
        
        self.assertEqual(Token.objects.all().count(), 1)