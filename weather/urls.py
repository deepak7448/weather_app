from django.urls import path
from django.conf.urls import include, url
from .import views
urlpatterns = [
    path('', views.location_weather, name='current'),
    path('search/',views.search,name='search')
   # path('countries/',views.countries,name='countries')
]