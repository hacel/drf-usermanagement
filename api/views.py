from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        for i, user in enumerate(queryset):
            serializer.data[i]["is_admin"] = user.groups.filter(
                name="Administrators"
            ).exists()
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = User.objects.create_user(
            data["username"], password=data.get("password"))
        if data.get("is_admin", False):
            user.groups.add(Group.objects.get(name="Administrators"))
        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]

    def retrieve(self, request, pk):
        user = self.get_object()
        serializer = UserSerializer(user)
        ret = {
            "username": serializer.data["username"],
            "is_admin": user.groups.filter(name="Administrators").exists(),
        }
        return Response(ret)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # Handle username
        if "username" in data:
            instance.username = data["username"]
        # Handle password
        if "password" in data:
            instance.set_password(data["password"])
        # Handle admin group
        if "is_admin" in data:
            if data["is_admin"]:
                instance.groups.add(Group.objects.get(name="Administrators"))
            else:
                instance.groups.remove(
                    Group.objects.get(name="Administrators"))
        instance.save()
        ret = {
            "username": data["username"],
            "is_admin": instance.groups.filter(name="Administrators").exists(),
        }
        return Response(ret)
