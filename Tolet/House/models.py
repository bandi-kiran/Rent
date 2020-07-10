from django.db import models
from django.contrib.auth.models import User


class HouseInfo(models.Model):
    #User = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=50)
    Phone = models.IntegerField(blank=True)
    Description = models.TextField(max_length=500)
    Price = models.FloatField()
    #Images = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.Address


class Image(models.Model):
    user = models.ForeignKey(HouseInfo,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='house_images')
