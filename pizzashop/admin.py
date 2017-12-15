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
    list_display = ['title', 'description', 'price', 'image_tag']
    # list_display = [field.name for field in Item._meta.fields]
    fields = ('title', 'description', 'price', 'image', 'image_tag')
    readonly_fields = ('image_tag',)
    search_fields = ['title', 'price', 'description']
    list_filter = ['price']

    class Meta:
        model = Item

    class Media:
        js = ('admin/js/admin.js',)
        css = {
            'all': ('admin/css/admin.css',)
        }


class OrderAdmin(admin.ModelAdmin):
    # list_display = ['customer', 'items', 'status']
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ['customer', 'status']
    list_filter = ['status']


class OrderItemAdmin (admin.ModelAdmin):
    # list_display = ['item', 'order', 'count', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']
    list_display = [field.name for field in OrderItem._meta.fields]
    # search_fields = ['order__id']
    search_fields = ['item', 'order__id', 'count', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']
    list_filter = ['order__id', 'order__customer__phone']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BasketItem)
