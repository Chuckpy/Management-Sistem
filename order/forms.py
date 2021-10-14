from django import forms
from order.models import SaleItem

class SaleForm(forms.Form):
    reference_code = forms.IntegerField(label='Código de Referência')
    customer = forms.ChoiceField(label='Cliente')
    discount = forms.DecimalField(label='Desconto', decimal_places=2, max_digits=5, )

class ProductForm(forms.Form):
    product_id = forms.CharField(label='Produto')
    quantity = forms.IntegerField(label='Quantidade')
    discount = forms.DecimalField(label='Desconto', max_digits=5, decimal_places=2)

class SaleItemModelForm(forms.ModelForm):
    sale = forms.CharField(label='Venda')
    product = forms.CharField(label='Produto')
    quantity = forms.IntegerField(label='Quantidade')
    discount = forms.DecimalField(label='Desconto', max_digits=5, decimal_places=2)
    class Meta:
        model = SaleItem
        fields = '__all__'
        