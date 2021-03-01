from api.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User, Group


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]


class RetrieveUserView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [DjangoModelPermissions]
