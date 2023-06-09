import django_filters

from .models import *

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields ='__all__'
        exclude = ['designation','quantity','qte_sortie','unite','emplacement','date_entree']

class RetourFilter(django_filters.FilterSet):
    class Meta:
        model = sortieMat1
        fields ='__all__'
       # exclude = ['designation','quantity','duree','date_sortie']
        exclude = ['designation','quantity','decharge','info', 'date_retour', 'date_sortie']

class HightTechFilter(django_filters.FilterSet):
    class Meta:
        model = hightech
        fields ='__all__'
       # exclude = ['designation','quantity','duree','date_sortie']
        exclude = ['marque','quantity','num_serie','user','imei','emplacement', 'arrivage', 'date_entree','emplacement']

class LaptopFilter(django_filters.FilterSet):
    class Meta:
        model = laptop
        fields ='__all__'
       # exclude = ['designation','quantity','duree','date_sortie']
        exclude = ['brand','quantity','num_serie','imei','user', 'date_entree','emplacement']