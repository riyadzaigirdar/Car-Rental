from django.urls import path
from booking import views
from django.contrib.auth.decorators import login_required
app_name = 'booking'

urlpatterns = [
    #path('add/', views.BookingView.as_view(), name='add_reservation'),
    path('add/<int:pk>/', login_required(views.BookingView.as_view()), name='add_reservation'),
]
