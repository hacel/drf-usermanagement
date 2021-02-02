from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    is_admin = serializers.BooleanField(required=False)
