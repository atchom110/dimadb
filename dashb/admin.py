from django.contrib import admin
from .models import Product, Category, hightech, laptop, sortieMat1
# Register your models here.

admin.site.site_header = 'DIMA STOCK DB DASHBOARD'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('designation','category','quantity','arrivage','date_entree','emplacement')

class laptopAdmin(admin.ModelAdmin):
    list_display = ('brand','num_serie','arrivage','date_entree','quantity')

class hightechAdmin(admin.ModelAdmin):
    list_display = ('marque','num_serie','imei','arrivage','date_entree','quantity')

class sortieAdmin(admin.ModelAdmin):
    list_display = ('designation','quantity','decharge','info','duree','date_sortie','retour','date_retour')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(hightech, hightechAdmin)
admin.site.register(laptop,laptopAdmin)
admin.site.register(sortieMat1,sortieAdmin)
