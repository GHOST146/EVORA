from django import forms


class Bookingform(forms.Form):
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YY', 'type' : 'date'}),
        label='Date',
        help_text='Enter the date in YYYY-MM-DD format.')