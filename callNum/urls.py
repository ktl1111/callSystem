from django.urls import path, include
from django.contrib import admin
from callNum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portal', views.portal, name='portal'),
    path('portal_onspot', views.portal_onspot, name='portal_onspot'),
    path('callnums', views.all_nums, name="list-nums"),
]