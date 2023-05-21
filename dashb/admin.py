from django.contrib import admin
from .models import Product, Category, SortieMat, hightech, laptop
# Register your models here.

admin.site.site_header = 'DIMA STOCK DB DASHBOARD'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('designation','category','quantity','emplacement')

class laptopAdmin(admin.ModelAdmin):
    list_display = ('brand','num_serie','quantity')

class hightechAdmin(admin.ModelAdmin):
    list_display = ('marque','num_serie','imei','quantity')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SortieMat)
admin.site.register(hightech, hightechAdmin)
admin.site.register(laptop,laptopAdmin)
