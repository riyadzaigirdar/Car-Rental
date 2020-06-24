from django.urls import path
from booking import views
app_name = 'booking'

urlpatterns = [
    path('add/', views.BookingView.as_view(), name='add_reservation'),
]