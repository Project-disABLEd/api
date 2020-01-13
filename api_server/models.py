from django.db import models

class Point(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ID = models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    source = models.TextField(max_length=100)
    desc = models.TextField(blank=True, default='')
    site = models.TextField(blank=True, default='')
    address = models.TextField()
    latitude = models.FloatField(max_length=10, blank=True, default='0')
    longitude = models.FloatField(max_length=10, blank=True, default='0')
    #opening_hours = models.DateTimeField()
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
