from django.contrib import admin

from cart.models import (
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

class ProductAdmin(admin.ModelAdmin):
    list_display = [
                    'title', 
                    'active',
                    'price', 
                    'stock', 
                    'updated']
    # list_filter = ['status']
    fieldsets = [
            (u'ColourVariation', {'fields': (
                    'title_en',
                    'slug_en',
                    'featured',
                    'available_colours',
                    'available_sizes',
                    'active',
                    'primary_category',
                    'secondary_categories',
                    'price', 
                    'stock', 
                    'title_fr',
                    'slug_fr',
                    
                    
            )})
        ]
    prepopulated_fields = {'slug_en': ('title_en',), 'slug_fr': ('title_fr',)}

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class SizeVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'SizeVariation', {'fields': ('name_en', 'name_fr',)})
        ]
        

class ColourVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'ColourVariation', {'fields': ('name_en', 'name_fr',)})
        ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Image)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ColourVariation,ColourVariationAdmin)
admin.site.register(SizeVariation,SizeVariationAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Payment)
