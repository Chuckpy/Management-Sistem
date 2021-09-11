from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from product.models import Product

class Sale(models.Model):
    reference_code = models.IntegerField('Código de Referência')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price= models.DecimalField('Preço', decimal_places=2, max_digits=10, default=0)
    discount = models.DecimalField('Desconto', decimal_places=2, max_digits=5, blank=True, default=0)
    nfe=models.BooleanField('Nota Fiscal Eletronica', default=False)
    date = models.DateField('Data',auto_now_add=True)
    
    
    def __str__(self):
        return f'Venda - {self.customer} - {self.id}'
    
    
    def total_price(self):  
        price = 00
        for product in self.product.all():
            price += product.price
        return (price - self.discount) # TODO : " - (self.impostos) "
    
    class Meta :
        verbose_name = "Vendas"
        verbose_name_plural = "Vendas"
        
class SaleItens(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.sale.reference_code} - {self.product.name}'
    
    class Meta :
        verbose_name = 'Item da Venda'
        verbose_name_plural = 'Itens da Venda'

class Order(models.Model): 
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE, related_name="sale", blank=True, null=True)   
    reference_code = models.IntegerField('Código de Referência')
    internal_code=models.IntegerField('Código Interno', blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.DecimalField('Preço',max_digits=10, decimal_places=2)
    description = models.TextField('Descição 1',max_length=500, blank=True)
    description_2 = models.TextField('Descição 2',max_length=500, blank=True)
    date = models.DateField('Data',auto_now_add=True)
    

    def __str__(self):
        return f'Ordem - {self.customer} - {self.id}'   
    
    class Meta :
        verbose_name = "Ordem"
        verbose_name_plural = "Ordens"
        
        