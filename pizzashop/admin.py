from django.contrib import admin

# Register your models here.
from pizzashop.models import Customer, Order, Item, OrderItem

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
