# from django.shortcuts import render

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissions

from api.serializers import UserSerializer, UserSerializer


@api_view(["GET", "POST"])
@csrf_exempt
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        for i, user in enumerate(users):
            serializer.data[i]["is_admin"] = user.groups.filter(
                name="Administrators"
            ).exists()
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
# @permission_classes([DjangoModelPermissions])
# @csrf_exempt
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "GET":
        serializer = UserSerializer(user)
        # serializer.data["is_admin"] = user.groups.filter(name="Administrators").exists()
        data = {
            "username": serializer.data["username"],
            "is_admin": user.groups.filter(name="Administrators").exists(),
        }
        return Response(data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)


# class UserList(APIView):
#     queryset = User.objects.all()

#     def get(self, request, format=None):
#         serializer = UserSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class UserDetail(APIView):
#     queryset = User.objects.all()

#     def get_object(self, pk):
#         return self.queryset.get(pk=pk)

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)