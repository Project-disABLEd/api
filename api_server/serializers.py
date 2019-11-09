from django.contrib.auth.models import Group, User
from rest_framework import serializers
from api_server.models import Point

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = dir(Point)
