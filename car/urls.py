from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
]