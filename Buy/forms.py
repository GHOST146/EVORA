from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="", max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your search term', 'class': 'home-btn'}))
    Name = forms.CharField(label="Name", required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'home-btn'}))
    Address = forms.CharField(label="Address", required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'home-btn'}))
    Residence = forms.CharField(label="Residency Type", required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'home-btn'}))
    Bedrooms = forms.IntegerField(label="Minimum Bedrooms", required=False, widget=forms.NumberInput(attrs={'class': 'home-btn'}))
    Bathrooms = forms.IntegerField(label="Minimum Bathrooms", required=False, widget=forms.NumberInput(attrs={'class': 'home-btn'}))
    Size = forms.IntegerField(label="Minimum Size", required=False, widget=forms.NumberInput(attrs={'class': 'home-btn'}))
    Min_price = forms.IntegerField(label="Minimum Price", required=False, widget=forms.NumberInput(attrs={'class': 'home-btn'}))
    Max_price = forms.IntegerField(label="Maximum Price", required=False, widget=forms.NumberInput(attrs={'class': 'home-btn'})) 
    BuyRent = forms.BooleanField(label="Buy or Rent", required=False)
    Image = forms.ImageField(label="Upload an image", required=False) 
    Image2 = forms.ImageField(label="Upload an image2", required=False) 
    Image3 = forms.ImageField(label="Upload an image3", required=False) 

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search'].error_messages = {'required': ''}