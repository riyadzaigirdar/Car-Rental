from django.shortcuts import render
from django.views.generic import ListView
from car.models import Car


class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car_list'
    paginate_by = 2
    queryset = Car.objects.all()