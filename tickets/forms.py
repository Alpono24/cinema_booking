from django import forms

class BookingForm(forms.Form):
    num_seats = forms.IntegerField(label="Количество мест:", min_value=1)