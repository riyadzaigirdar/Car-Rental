from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from booking.models import QuickBookingCar, ExtraBenifit
from car.models import Car
import datetime


# class BookingView(LoginRequiredMixin, CreateView):
#     model = BookingCar
#     form_class = BookingCarForm
#     template_name = 'booking/reservation.html'
#     success_url = 'home:home'
   

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['car'] = Car.objects.get(pk=self.kwargs['pk'])
#         context['benifits'] = ExtraBenifit.objects.all()
#         return context

#     def form_valid(self, form):
#         print("yes")
#         benifit = form.cleaned_data['extra_benifit']

#         booking_obj = form.save(commit=False)
#         booking_obj.customer = self.request.user

#         car_obj = Car.objects.get(pk=self.kwargs['pk'])
#         booking_obj.car = car_obj
#         print(booking_obj)
#         booking_obj.save()

#         booking_obj.extra_benifits.add(benifit)

#         booking_obj.save_m2m()
#         super(BookingView, self).form_valid(form)


class BookingView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {
            'car': Car.objects.get(pk=self.kwargs['pk']),
            'benifits': ExtraBenifit.objects.all()
        }
        return render(request, "booking/reservation.html", context)

    def post(self, request, *args, **kwargs):
        car = Car.objects.get(pk=self.kwargs['pk'])
        booking = QuickBookingCar(car=car)

        if(request.POST['pickupdate']):
            list1 = request.POST['pickupdate'].split('/')
            date1 = list1[2] +'-'+ list1[0] +'-'+list1[1]
            booking.pickup_date = date1
        
        booking.pickup_location = request.POST['pickup'] 
        
        if (request.POST['picktime']):
            list3 = request.POST['picktime'].split(":")
            list4 = list3[1].split(" ")
            time1 = list3[0] + ':' + list4[1]
            time1 = time1.replace(" ","")
            time1 = (datetime.datetime.strptime(time1+":00.00", '%H:%M:%S.%f'))
            booking.pickup_time = time1.time()


        booking.drop_off_location = request.POST['dropoff']

        if(request.POST['dropoffdate']):
            list2 = request.POST['dropoffdate'].split('/')
            date2 = list2[2] +'-'+ list2[0] +'-'+list2[1]           
            booking.drop_off_date = date2          

        if (request.POST['droptime']):
            list5 = request.POST['droptime'].split(":")
            list6 = list5[1].split(" ")
            time2 = list5[0] + ':' + list6[1] 
            time2 = time2.replace(" ","")
            time2 = (datetime.datetime.strptime(time2+":00.00", '%H:%M:%S.%f'))
            booking.drop_off_time = time2.time()

        booking.info = request.POST['addinfo']
        booking.payment = request.POST['payment']
        booking.save()

        if(request.POST.get('Televission Per Day')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Televission Per Day"))
        if(request.POST.get('Backfast & Lunch Per Day')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Backfast & Lunch Per Day"))
        if(request.POST.get('Childen Seat')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Childen Seat"))
        if(request.POST.get('Car Insurances')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Car Insurances"))
        if(request.POST.get('Air-Condition Per Day')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Air-Condition Per Day"))
        if(request.POST.get('Security & Safety')):
            booking.benifits.add(ExtraBenifit.objects.get(name="Security & Safety"))
        
        booking.save()

        return render(request, "home/index.html")        
