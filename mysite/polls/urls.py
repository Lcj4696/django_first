# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:51:29 2022

@author: 82103
"""

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    ]