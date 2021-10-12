from django import forms

class SaleForm(forms.Form):
    reference_code = forms.IntegerField(label='Código de Referência')
    customer = forms.ChoiceField(label='Cliente')
    discount = forms.DecimalField(label='Desconto', decimal_places=2, max_digits=5, )

class ProductForm(forms.Form):
    product_id = forms.CharField(label='Produto')
    quantity = forms.IntegerField(label='Quantidade')
    discount = forms.DecimalField(label='Desconto', max_digits=5, decimal_places=2)
