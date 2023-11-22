import os
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = "Setup user and display token"

    def handle(self, *args, **options):
        tokens = Token.objects.all()
        if tokens.count():
            self.stdout.write(
                self.style.SUCCESS(f"Token tokens[0].key")
            )
        else:
            user = User.objects.create_user(
                username=os.environ.get("EMAIL_ADDRESS", "piotr").split("@")[0],
                email=os.environ.get("EMAIL_ADDRESS", "piotr@example.com"),
                password=os.environ.get("EMAIL_PASSWORD", "super-secret"),
            )
            token = Token.objects.create(user=user)
            self.stdout.write(
                self.style.SUCCESS(f"Token {token.key}")
            )