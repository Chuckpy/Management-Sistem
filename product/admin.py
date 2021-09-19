from django.contrib import admin
from .models import Product,  Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados do produto :', {
            'fields':('image','name', 'category', 'description', 'reference_code')
        } ),
        ('Dados de preço :', {
          'fields':('price', 'is_available')  
        } )
    )
    list_filter= ('id', 'category', 'price')
    list_display = ('id','image', 'name','description','price' ) 
    search_fields = ('id', 'name', 'reference_code', 'internal_code')
    
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)