from django import forms

from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            # 'slug',
            'featured',
            'description',
            'price',
            'available_colours',
            'available_sizes',
            # 'primary_category',
            # 'secondary_categories',
        ]
