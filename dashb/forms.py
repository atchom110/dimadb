from django import forms
from .models import Product, hightech, laptop

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['designation','category','quantity','unite','emplacement']

class HightechForm(forms.ModelForm):
    class Meta:
        model = hightech
        fields = ['marque','num_serie','imei','quantity','emplacement']

class LaptopForm(forms.ModelForm):
    class Meta:
        model = laptop
        fields = ['brand','num_serie','imei','quantity','emplacement']