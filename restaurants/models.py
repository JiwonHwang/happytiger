from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    rating = models.FloatField()
    description = models.TextField()
    address = models.TextField()
    country = models.CharField(max_length=30)
    album = models.ForeignKey(
        'Photo',
    )
    reviews = models.ForeignKey(
        'Review',
    )

class Photo(models.Model):
    date = models.DateField(auto_now=True)
    photo = models.ImageField()

class Review(models.Model):
    user = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    ratings = models.FloatField()
    date = models.DateField(auto_now=True)
    comment = models.TextField()
