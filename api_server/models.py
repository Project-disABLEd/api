from django.db import models
from api_server.validators import validate_rating, validate_url, validate_latitude, validate_longitude

class Point(models.Model):
    created = models.DateTimeField(auto_now_add=True) # Auto-created, returns date of creation
    ID = models.AutoField(verbose_name='ID', primary_key=True, auto_created=True) # Auto-generated ID
    name = models.CharField(max_length=100) # Name of the place, required
    source = models.TextField(max_length=100) # Source from which the data was taken (Manual,
                                              # OpenStreetMap/WheelMap/accessibility.cloud, Town Hall), required
    desc = models.TextField(blank=True, default='') # Description of the place, optional
    site = models.TextField(blank=True, default='', validators=[validate_url]) # WWW site of the place, optional
    address = models.TextField(blank=True, default='') # Address of the place, optional
    latitude = models.FloatField(max_length=10, validators=[validate_latitude]) # Latitude, required
    longitude = models.FloatField(max_length=10, validators=[validate_longitude]) # Longitude, required
    typeObj = models.ForeignKey('TypeOfPoint', on_delete=models.CASCADE) # Type of point, required
    #opening_hours = models.DateTimeField()

    '''
    Below are the disability specific fields. Due to uncertainity of some parameters, all fields are optional.
    
    All of them use a following format for the main Integer field:
    - 2 - The place fully supports the thing in question.
    - 1 - The place partially supports the thing in question. (ex. cinemas allowing/providing places for disabled people on wheelchairs only on the lowest rows)
    - 0 - Unknown support by the place.
    - -1 - The place does not support the thing in question.
    '''
    maxLengthForDesc = 200 # Max length for all text fields below.
    
    wheelchair_accessibility = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    wheelchair_accessibility_desc = models.TextField(blank=True, default='')

    toilets = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    toilets_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    discounts = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    discounts_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    guide_dog = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    guide_dog_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    parking = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    parking_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    hearing_imp = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    hearing_imp_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    vision_imp = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    vision_imp_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    mental_disorder = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    mental_disorder_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)

    staff = models.IntegerField(blank=True, default='0', validators=[validate_rating])
    staff_desc = models.TextField(blank=True, default='', max_length=maxLengthForDesc)


    class Meta:
        ordering = ['ID']
        

class TypeOfPoint(models.Model):
    name = models.TextField(max_length=100)