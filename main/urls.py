from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('car_detail/', views.car_detail, name='car_detail'),
    path('manufacturer_detail/', views.manufacturer_detail, name='manufacturer_detail'),
]
