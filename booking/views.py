from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from booking.forms import BookingCarForm
from booking.models import BookingCar
from car.models import Car


class BookingView(LoginRequiredMixin, CreateView):
    model = BookingCar
    form_class = BookingCarForm
    template_name = 'booking/reservation.html'
    success_url = 'home:home'
    #redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):

        booking_obj = form.save(commit=False)
        booking_obj.customer = self.request.user
        #booking_obj.extra_benifits=
        booking_obj.save()
        super(BookingView, self).form_valid(form)

    
