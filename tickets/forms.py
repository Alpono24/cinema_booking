from django import forms

class BookingForm(forms.Form):
    selected_seats = forms.MultipleChoiceField(label="Выберите места", widget=forms.CheckboxSelectMultiple)

    def clean_selected_seats(self):
        seats = self.cleaned_data['selected_seats']
        # Любые дополнительные проверки
        return seats

class BookingForm(forms.Form):
   selected_seats = forms.MultipleChoiceField(label="Выберите места:", widget=forms.CheckboxSelectMultiple)

   def __init__(self, *args, **kwargs):
       free_seats = kwargs.pop('free_seats', [])
       super().__init__(*args, **kwargs)
       self.fields['selected_seats'].choices = [(s, s) for s in free_seats]