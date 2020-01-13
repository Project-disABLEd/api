from django.db import models

class Point(models.Model):
    created = models.DateTimeField(auto_now_add=True) # Auto-created, returns date of creation
    ID = models.AutoField(verbose_name='ID', primary_key=True, auto_created=True) # Auto-generated ID
    name = models.CharField(max_length=100) # Name of the place, required
    source = models.TextField(max_length=100) # Source from which the data was taken (Manual, OpenStreetMap/WheelMap/accessibility.cloud, Town Hall), required
    desc = models.TextField(blank=True, default='') # Description of the place, optional
    site = models.TextField(blank=True, default='') # WWW site of the place, optional
    address = models.TextField() # Address of the place, required
    latitude = models.FloatField(max_length=10, blank=True, default='0') # Latitude, optional (will be converted from the address ASAP by the curation team)
    longitude = models.FloatField(max_length=10, blank=True, default='0') # Longitude, optional (will be converted from the address ASAP by the curation team)
    #opening_hours = models.DateTimeField()

    '''
    Below are the disability specific fields. Due to uncertainity of some parameters, all fields are optional.
    
    All of them use a following format for the main Integer field:
    - 2 - The place fully supports the thing in question.
    - 1 - The place partially supports the thing in question. (ex. cinemas allowing/providing places for disabled people on wheelchairs only on the lowest rows)
    - 0 - Unknown support by the place.
    - -1 - The place does not support the thing in question.
    '''

    wheelchair_accessibility = models.IntegerField(blank=True, default='0')
    wheelchair_accessibility_desc = models.TextField(blank=True)
    toilets = models.IntegerField(blank=True, default='0')
    toilets_desc = models.TextField(blank=True, default='')
    discounts = models.IntegerField(blank=True, default='0')
    discounts_desc = models.TextField(blank=True, default='')
    guide_dog = models.IntegerField(blank=True, default='0')
    guide_dog_desc = models.TextField(blank=True, default='')
    parking = models.IntegerField(blank=True, default='0')
    parking_desc = models.TextField(blank=True, default='')
    hearing_imp = models.IntegerField(blank=True, default='0')
    hearing_imp_desc = models.TextField(blank=True, default='')
    vision_imp = models.IntegerField(blank=True, default='0')
    vision_imp_desc = models.TextField(blank=True, default='')
    mental_disorder = models.IntegerField(blank=True, default='0')
    mental_disorder_desc = models.TextField(blank=True, default='')
    staff = models.IntegerField(blank=True, default='0')
    staff_desc = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['ID']
