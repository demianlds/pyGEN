from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'category', 'actual_stock', 'min_stock', 'price']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']
