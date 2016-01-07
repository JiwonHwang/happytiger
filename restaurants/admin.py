from django.contrib import admin

# Register your models here.
from .models import Restaurant, Photo, Review
admin.site.register(Restaurant)
admin.site.register(Photo)
admin.site.register(Review)
