from django.urls import re_path
from accounts.views import ReadLastUnseenEmail, SendEmail

api_urlpatterns = [
    re_path("last_unseen_email", ReadLastUnseenEmail.as_view()),
    re_path("send_email", SendEmail.as_view()),
]