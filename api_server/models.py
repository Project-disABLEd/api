from django.db import models

class Point(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ID = models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    site = models.TextField(default='')
    address = models.TextField()
    latitude = models.FloatField(max_length=10, blank=True, default='0')
    longitude = models.FloatField(max_length=10, blank=True, default='0')
    #opening_hours = models.DateTimeField()
    wheelchair_accessibility = models.IntegerField(blank=True, default='0')
    wheelchair_accessibility_desc = models.TextField()
    toilets = models.IntegerField(blank=True, default='0')
    toilets_desc = models.TextField()
    discounts = models.IntegerField(blank=True, default='0')
    discounts_desc = models.TextField()
    guide_dog = models.IntegerField(blank=True, default='0')
    guide_dog_desc = models.TextField()
    parking = models.IntegerField(blank=True, default='0')
    parking_desc = models.TextField()
    hearing_imp = models.IntegerField(blank=True, default='0')
    hearing_imp_desc = models.TextField()
    vision_imp = models.IntegerField(blank=True, default='0')
    vision_imp_desc = models.TextField()
    mental_disorder = models.IntegerField(blank=True, default='0')
    mental_disorder_desc = models.TextField()
    staff = models.IntegerField(blank=True, default='0')
    staff_desc = models.TextField()

    class Meta:
        ordering = ['ID']
