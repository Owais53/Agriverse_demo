# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views



urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('map/',views.map,name='map'),
    path('map_change/',views.map_change,name='map_change'),
    path('pixel_map/',views.pixel_map,name='map_pixel'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
