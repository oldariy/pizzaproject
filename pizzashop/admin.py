from django.contrib import admin
from pizzashop.models import Customer, Order, Item, OrderItem, BasketItem


class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'phone', 'address']
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = ['phone', 'address', 'last_name']
    list_filter = ['phone']

    class Meta:
        model = Customer

class ItemAdmin (admin.ModelAdmin):
    #list_display = ['title', 'description', 'price', 'image', 'imgfile']
    list_display = [field.name for field in Item._meta.fields]
    fields = ('title', 'description', 'price', 'image', 'image_tag',)
    readonly_fields = ('image_tag',)
    search_fields  = ['title', 'price', 'description']
    list_filter = ['price']

    class Meta:
        model = Item

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BasketItem)
