from django.shortcuts import render
from .models import Restaurant, Photo, Review

def homepage(request):
    album = Photo.objects.all().order_by("date")[:3]
    new_review = Review.objects.all().order_by("date")[:3]
    return render(request, 'restaurants/homepage.html', {"album": album, "new_review": new_review})

def about(request):
    return render(request, 'restaurants/about.html')

def restaurants(request):
    return render(request, 'restaurants/restaurants.html')
