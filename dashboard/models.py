from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.db.models import Sum, Count, F
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})

    class Meta :
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Product(models.Model):
    
    name = models.CharField('Nome',max_length=100, null=True)
    category = models.ManyToManyField(Category, related_name="category", blank=True)
    description = models.TextField('Descrição',max_length=500, blank=True)
    reference_code = models.IntegerField('Código de Referência')
    internal_code=models.IntegerField('Código Interno',blank=True, null=True)
    price = models.DecimalField('Preço',max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Quantidade',null=True)
    image = models.ImageField('Imagem', upload_to="products/%Y/%m/%d", blank=True)
    is_available = models.BooleanField('Disponivel', default=True)

    objects = models.Manager()
    available = AvailableManager()
    
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
        
    class Meta :
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Sale(models.Model):
    reference_code = models.IntegerField('Código de Referência')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price= models.DecimalField('Preço', decimal_places=2, max_digits=10, default=0)
    discount = models.DecimalField('Desconto', decimal_places=2, max_digits=5, blank=True, default=0)
    nfe=models.BooleanField('Nota Fiscal Eletronica', default=False)
    product = models.ManyToManyField(Product,related_name="product", blank=True)
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
        
        

@receiver(m2m_changed, sender=Sale.product.through)
def update_sale_price(sender, instance, **kwargs):
    instance.price =  instance.total_price()
    instance.save()