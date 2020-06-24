from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_details', kwargs={'pk': self.pk})


class Car(models.Model):
    GEAR_CHOICES = (
        ('auto', 'Auto'),
        ('manula', 'Manual'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    car_category = models.ManyToManyField(Category, related_name='car_category', blank=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    car_image = models.ImageField(upload_to='car', blank=True, null=True)
    car_mileage = models.PositiveIntegerField(blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    gear = models.CharField(max_length=10, choices=GEAR_CHOICES, default='auto', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_details', kwargs={'pk': self.pk})
