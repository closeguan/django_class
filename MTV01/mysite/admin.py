from django.contrib import admin
from .models import Product ,NewTable
from mysite.models import Product, NewTable 
#admin.site.register(NewTable)
#admin.site.register(Product)

#
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','qty')



class NewTableAdmin(admin.ModelAdmin):
    list_display = ('char_f','date_f','datetime_f')

admin.site.register(Product, ProductAdmin)
admin.site.register(NewTable, NewTableAdmin)
