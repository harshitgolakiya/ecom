from django.contrib import admin

from .models import product,order,customer,category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

admin.site.register(product,ProductAdmin)
admin.site.register(order)
admin.site.register(customer)
admin.site.register(category)