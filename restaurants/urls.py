from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^$', views.about, name='about'),
    url(r'^$', views.restaurants, name='restaurants'),
]
