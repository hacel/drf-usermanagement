from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    is_admin = serializers.BooleanField(required=False)

    def create(self, validated_data):
        if "password" not in validated_data:
            raise
        user = User.objects.create_user(
            validated_data["username"], password=validated_data.get("password")
        )
        if validated_data.get("is_admin", False):
            user.groups.add(Group.objects.get(name="Administrators"))
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        # if instance.check_password(validated_data.get("password")):
        # instance.set_password(validated_data.get("password"))
        make_admin = validated_data.get("is_admin")
        if make_admin is not None:
            if make_admin is True:
                instance.groups.add(Group.objects.get(name="Administrators"))
            else:
                instance.groups.remove(Group.objects.get(name="Administrators"))
        instance.save()
        return instance


"""
{
    "username": "11",
    "password": "inr2u3",
    "is_admin": true
}
"""