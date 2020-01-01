from django.contrib.auth.models import User, Group
from django import forms
from rest_framework import viewsets
from api_server.models import Point
from django.shortcuts import render
from api_server.serializers import UserSerializer, GroupSerializer, PointSerializer

def map_view(*args, **kwargs):
	print(args, kwargs)
	return render(request, "mapa.html", {})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Point.objects.all().order_by('-ID')
    serializer_class = PointSerializer
