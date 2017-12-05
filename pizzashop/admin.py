from django.contrib import admin
from pizzashop.models import Customer, Order, Item, OrderItem, BasketItem


class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'phone', 'address']
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = ['phone', 'address', 'last_name']
    list_filter = ['phone']

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BasketItem)
