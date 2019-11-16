from django.contrib import admin
from .models import Product
from mysite.models import NewTable, Product 
#admin.site.register(NewTable)
#admin.site.register(Product)

#
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','qty')

admin.site.register(Product, ProductAdmin)