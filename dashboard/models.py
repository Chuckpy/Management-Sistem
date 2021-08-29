from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

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


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField(Category, related_name="products")
    description = models.TextField(max_length=500, blank=True)
    reference_code = models.IntegerField()
    internal_code=models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()
    
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})


class Order(models.Model): 
    sale = models.ForeignKey(Product, related_name="sale", on_delete=models.CASCADE)   
    reference_code = models.IntegerField()
    internal_code=models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    description_2 = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}testes'