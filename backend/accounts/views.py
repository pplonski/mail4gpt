from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
    inline_serializer,
)
from drf_spectacular.types import OpenApiTypes

from rest_framework import serializers
from accounts.email import EmailService


class EmailSerializer(serializers.Serializer):
    from_address = serializers.EmailField()
    date = serializers.DateTimeField()
    subject = serializers.CharField()
    body = serializers.CharField()


class EmailSentInfoSerializer(serializers.Serializer):
    status = serializers.CharField()


class ReadEmail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmailSerializer

    @extend_schema(
        request=inline_serializer(
            name="ReadEmailSerializer",
            fields={
                "latest_count": serializers.IntegerField(),
                "show_unseen": serializers.BooleanField(),
            },
        ),
    )
    def post(self, request, format=None):
        latest_count = int(request.data.get("latest_count", 5))
        show_unseen = request.data.get("show_unseen", True)
        criteria = "UNSEEN" if show_unseen else "ALL"
        m = EmailService()
        emails = m.get_emails(criteria=criteria, latest_count=latest_count)

        return Response(
            emails,
            status.HTTP_200_OK,
        )


class SendEmail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmailSentInfoSerializer

    @extend_schema(
        request=inline_serializer(
            name="SendEmailSerializer",
            fields={
                "to": serializers.EmailField(),
                "subject": serializers.CharField(),
                "body": serializers.CharField(),
            },
        ),
    )
    def post(self, request, format=None):
        to_address = request.data.get("to", "")
        subject = request.data.get("subject", "")
        body = request.data.get("body", "")

        if "@" not in to_address:
            return Response(
                {"msg": "Error when sending email. Wrong email address"},
                status.HTTP_400_BAD_REQUEST,
            )
        
        m = EmailService()
        m.send(to_address, subject, body)

        return Response(
            {"msg": "Email sent successfully"},
            status.HTTP_200_OK,
        )
