from django.contrib import admin

from .models import (
    Payment,
    Product, 
    OrderItem, 
    Order,
    ColourVariation,
    SizeVariation,
    Address,
    Payment,
    Category,
    Image,
    Comment,
   
    )


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'user', 'product', 'rate', 'id')


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ColourVariation)
admin.site.register(SizeVariation)
admin.site.register(Address, AddressAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Payment)
