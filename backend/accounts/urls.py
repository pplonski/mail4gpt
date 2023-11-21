from django.urls import re_path
from accounts.views import ReadEmail, SendEmail

api_urlpatterns = [
    re_path("read_email", ReadEmail.as_view()),
    re_path("send_email", SendEmail.as_view()),
]