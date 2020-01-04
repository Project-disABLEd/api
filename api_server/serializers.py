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
        ##fields = dir(Point)
        fields = [
            'name',
			'source',
            'desc',
            'site',
            'address',
            'latitude',
            'latitude',
            'longitude',
            'wheelchair_accessibility',
            'wheelchair_accessibility_desc',
            'toilets',
            'toilets_desc',
            'discounts',
            'discounts_desc',
            'guide_dog',
            'guide_dog_desc',
            'parking',
            'parking_desc',
            'hearing_imp',
            'hearing_imp_desc',
            'vision_imp',
            'vision_imp_desc',
            'mental_disorder',
            'mental_disorder_desc',
            'staff',
            'staff_desc'
            ]
