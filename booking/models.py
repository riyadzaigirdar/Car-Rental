from django.db import models
from django.urls import reverse

from accounts.models import User
from car.models import Car


class ExtraBenifit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class QuickBookingCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='quick_booking_car')
    pickup_location = models.CharField(max_length=100, blank=True, null=True)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    drop_off_location = models.CharField(max_length=100, blank=True, null=True)
    drop_off_date = models.DateField()
    drop_off_time = models.TimeField()

    def __str__(self):
        return str(self.pickup_date)

    def get_absolute_url(self):
        return reverse('quickbooking_details', kwargs={'pk': self.pk})


class BookingCar(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('paypal', 'PayPal'),
        ('payoneer', 'Payoneer'),
        ('visacard', 'Visa Card'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_profile')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, default='paypal', blank=True, null=True)
    additional_info = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='booking_car')
    extra_benifits = models.ManyToManyField(ExtraBenifit, related_name='extra_benifit')
    pickup_location = models.CharField(max_length=100, blank=True, null=True)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    drop_off_location = models.CharField(max_length=100, blank=True, null=True)
    drop_off_date = models.DateField()
    drop_off_time = models.TimeField()
    quick_booking = models.ManyToManyField(QuickBookingCar, blank=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.email

    def get_absolute_url(self):
        return reverse('booking_details', kwargs={'pk': self.pk})
