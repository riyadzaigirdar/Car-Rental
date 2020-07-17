from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from booking.forms import BookingCarForm
from booking.models import BookingCar, ExtraBenifit
from car.models import Car


class BookingView(LoginRequiredMixin, CreateView):
    model = BookingCar
    form_class = BookingCarForm
    template_name = 'booking/reservation.html'
    success_url = 'home:home'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs['pk'])
        context['benifits'] = ExtraBenifit.objects.all()
        return context

    def form_valid(self, form):
        benifit = form.cleaned_data['extra_benifit']

        booking_obj = form.save(commit=False)
        booking_obj.customer = self.request.user

        car_obj = Car.objects.get(pk=self.kwargs['pk'])
        booking_obj.car = car_obj
        print(booking_obj)
        booking_obj.save()

        booking_obj.extra_benifits.add(benifit)

        booking_obj.save_m2m()
        super(BookingView, self).form_valid(form)

    
