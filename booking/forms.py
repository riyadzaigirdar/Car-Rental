from django.forms import ModelForm, MultipleChoiceField,CheckboxSelectMultiple
from booking.models import BookingCar, ExtraBenifit


class BookingCarForm(ModelForm):
    class Meta:
        model = BookingCar
        exclude = ['ordered', 'delevered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pickup_location'].widget.attrs.update(
            {'class': 'form-control has-icon', 'placeholder': 'Pickup Location'})
        self.fields['drop_off_location'].widget.attrs.update(
            {'class': 'form-control has-icon', 'placeholder': 'Drop Off Location'})
        self.fields['pickup_date'].widget.attrs.update(
            {'class': 'form-control has-icon datepicker-here', 'placeholder': 'Pickup Date'})
        self.fields['pickup_time'].widget.attrs.update(
            {'class': 'form-control has-icon timepicker', 'placeholder': 'Pickup Time'})
        self.fields['drop_off_date'].widget.attrs.update(
            {'class': 'form-control has-icon datepicker-here', 'placeholder': 'Drop Off Date'})
        self.fields['drop_off_time'].widget.attrs.update(
            {'class': 'form-control has-icon timepicker', 'placeholder': 'Drop Off Time'})
        #self.fields["extra_benifits"].queryset = ExtraBenifit.objects.all()
        #self.fields["extra_benifits"].widget = CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
