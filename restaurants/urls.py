from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about$', views.about, name='about'),
    url(r'^restaurants$', views.restaurants, name='restaurants'),
]
