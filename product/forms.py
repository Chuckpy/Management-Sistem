from django import forms
from .models import Product
from order.models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','description', 'reference_code', 'price', 'quantity', 'image', 'is_available']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['sale', 'reference_code', 'price', 'customer', 'description', 'description_2']