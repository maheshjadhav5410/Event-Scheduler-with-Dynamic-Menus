from django import forms
from events.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','event', 'venue_type', 'date', 'time_slot', 'total_persons']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-select'}),
            'event': forms.Select(attrs={'class': 'form-select'}),
            'venue_type': forms.Select(attrs={'class': 'form-select'}),
            'total_persons': forms.NumberInput(attrs={'class': 'form-control'}),
        }
