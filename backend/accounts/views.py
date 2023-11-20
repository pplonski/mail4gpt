from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, inline_serializer
from drf_spectacular.types import OpenApiTypes


from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    from_email = serializers.EmailField()
    date = serializers.DateTimeField()
    content = serializers.CharField()

class EmailSentInfoSerializer(serializers.Serializer):
    status = serializers.CharField()

class ReadLastUnseenEmail(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmailSerializer

    def post(self, request, format=None):
        return Response(
            {
            },
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
        return Response(
            {
            },
            status.HTTP_200_OK,
        )
    