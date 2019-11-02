from django.contrib.auth.models import User, Group
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

class PointSerializer(serializers.Serializer):
    ID = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    site = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(required=True)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    #opening_hours = serializers.DateTimeField()
    wheelchair_accessibility = serializers.IntegerField(required=False)
    wheelchair_accessibility_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    toilets = serializers.IntegerField(required=False)
    toilets_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    discounts = serializers.IntegerField(required=False)
    discounts_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    guide_dog = serializers.IntegerField(required=False)
    guide_dog_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    parking = serializers.IntegerField(required=False)
    parking_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    hearing_imp = serializers.IntegerField(required=False)
    hearing_imp_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    vision_imp = serializers.IntegerField(required=False)
    vision_imp_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    mental_disorder = serializers.IntegerField(required=False)
    mental_disorder_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    staff = serializers.IntegerField(required=False)
    staff_desc = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Point` instance, given the validated data.
        """
        return Point.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Point` instance, given the validated data.
        """
        instance.ID = validated_data.get('ID', instance.ID)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.address = validated_data.get('address', instance.address)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        #instance.opening_hours = serializers.DateTimeField()
        instance.wheelchair_accessibility = validated_data.get('wheelchair_accessibility', instance.wheelchair_accessibility)
        instance.wheelchair_accessibility_desc = validated_data.get('wheelchair_accessibility_desc', instance.wheelchair_accessibility_desc)
        instance.toilets = validated_data.get('toilets', instance.toilets)
        instance.toilets_desc = validated_data.get('toilets_desc', instance.toilets_desc)
        instance.discounts = validated_data.get('discounts', instance.discounts)
        instance.discounts_desc = validated_data.get('discounts_desc', instance.discounts_desc)
        instance.guide_dog = validated_data.get('guide_dog', instance.guide_dog)
        instance.guide_dog_desc = validated_data.get('guide_dog_desc', instance.guide_dog_desc)
        instance.parking = validated_data.get('parking', instance.parking)
        instance.parking_desc = validated_data.get('parking_desc', instance.parking_desc)
        instance.hearing_imp = validated_data.get('hearing_imp', instance.hearing_imp)
        instance.hearing_imp_desc = validated_data.get('hearing_imp_desc', instance.hearing_imp_desc)
        instance.vision_imp = validated_data.get('vision_imp', instance.vision_imp)
        instance.vision_imp_desc = validated_data.get('vision_imp_desc', instance.vision_imp_desc)
        instance.mental_disorder = validated_data.get('mental_disorder', instance.mental_disorder)
        instance.mental_disorder_desc = validated_data.get('mental_disorder_desc', instance.mental_disorder_desc)
        instance.staff = validated_data.get('staff', instance.staff)
        instance.staff_desc = validated_data.get('staff_desc', instance.staff_desc)
        instance.save()
        return instance

    #class Meta:
    #    model = Point
    #    fields = ['url', 'name']
