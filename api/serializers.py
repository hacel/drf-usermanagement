from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    is_admin = serializers.BooleanField(required=False)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['is_admin'] = instance.groups.filter(
            name="Administrators").exists()
        return ret

    def create(self, validated_data):
        # if "password" not in validated_data:
        #     raise
        user = User.objects.create_user(
            validated_data["username"], password=validated_data.get("password")
        )
        if validated_data.get("is_admin", False):
            user.groups.add(Group.objects.get(name="Administrators"))
        return user

    def update(self, instance, validated_data):
        # Handle username
        if "username" in validated_data:
            instance.username = validated_data["username"]
        # Handle password
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        # Handle admin group
        if "is_admin" in validated_data:
            if validated_data["is_admin"]:
                instance.groups.add(Group.objects.get(name="Administrators"))
            else:
                instance.groups.remove(
                    Group.objects.get(name="Administrators"))
        instance.save()
        return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
