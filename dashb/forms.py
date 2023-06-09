from django import forms
from .models import Product, hightech, laptop, sortieMat1

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['designation','category','quantity','qte_sortie','unite','arrivage','date_entree','emplacement']

class HightechForm(forms.ModelForm):
    class Meta:
        model = hightech
        fields = ['marque','num_serie','imei','quantity','arrivage','date_entree','emplacement']

class PhoneForm(forms.ModelForm):
    class Meta:
        model = hightech
        fields = ['marque','num_serie','imei','user','arrivage','date_entree','sortie','emplacement']

class TabForm(forms.ModelForm):
    class Meta:
        model = hightech
        fields = ['marque','num_serie','imei','user','arrivage','date_entree','sortie','emplacement']

class LaptopForm(forms.ModelForm):
    class Meta:
        model = laptop
        fields = ['brand','num_serie','imei','user','arrivage','date_entree','sortie','emplacement']

class SortieMatForm(forms.ModelForm):
    date_sortie = forms.DateTimeField(required=False)
    date_retour = forms.DateField(required=False)
    class Meta:
        model = sortieMat1
        fields = ['designation','quantity','decharge','info','duree','date_sortie','retour','date_retour']