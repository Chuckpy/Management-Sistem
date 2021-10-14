from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum, F, FloatField
from django.db.models.signals import post_save
from django.dispatch import receiver
from autoslug import AutoSlugField

from .managers import SaleManager
from product.models import Product

STATUS = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado'),
    )   

class Sale(models.Model):     
    reference_code = models.IntegerField('Código de Referência')
    slug = AutoSlugField(unique=True, always_update=False, populate_from="reference_code", default=None)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price= models.DecimalField('Preço', decimal_places=2, max_digits=10, default=0)
    discount = models.DecimalField('Desconto', decimal_places=2, max_digits=5, blank=True, default=0)
    nfe=models.BooleanField('Nota Fiscal Eletronica', default=False)
    status = models.CharField('Status',choices=STATUS,max_length=50, null=True, blank=True)
    date = models.DateField('Data',auto_now_add=True)
    
    objects= SaleManager()
    
    def __str__(self):
        return f'Venda - {self.id}'
    
    def get_absolute_url(self):
        return reverse("order:detail", kwargs={"slug": self.slug})
    
    def total_price(self): 
        total = self.saleitem_set.all().aggregate(
            total_sale=Sum((F('quantity')* F('product__price')) - F('discount'), output_field=FloatField())
        )['total_sale'] or 0
        total = total - float(self.discount) # TODO - self.imposto
        self.price = total
        Sale.objects.filter(id=self.id).update(price=total)        
    
    def products(self):
        products = self.saleitem_set.all()
        return products     
   
    class Meta :
        permissions = (
            ('nfe_change', 'Usuário pode alterar parâmetro NF-e'),
        )
        verbose_name = "Vendas"
        verbose_name_plural = "Vendas"
        
class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.product.name} - {self.sale.id}'
    
    class Meta :
        verbose_name = 'Item da Venda'
        verbose_name_plural = 'Itens da Venda'

class Order(models.Model): 
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE, related_name="sale", blank=True, null=True,)   
    slug = AutoSlugField(unique=True, always_update=False, populate_from="customer", default=None)
    reference_code = models.IntegerField('Código de Referência')
    internal_code=models.IntegerField('Código Interno', blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField('Preço',max_digits=10, decimal_places=2)
    description = models.TextField('Descição 1',max_length=500, blank=True)
    description_2 = models.TextField('Descição 2',max_length=500, blank=True)
    date = models.DateField('Data',auto_now_add=True)

    def __str__(self):
        return f'Ordem - {self.customer} - {self.id}'   
    
    class Meta :
        verbose_name = "Ordem"
        verbose_name_plural = "Ordens"
        
        
@receiver(post_save, sender=SaleItem)
def update_sale_price(sender, instance,**kwargs):
    instance.sale.total_price()
        
@receiver(post_save, sender=Sale)
def update_sale_price2(sender, instance,**kwargs):
    instance.total_price()