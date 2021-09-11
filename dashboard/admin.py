from django.contrib import admin

# TODO (apagar :)
# from .models import Product, Order, Category, Sale, SaleItens
# from .actions import nfe_nao_emitida, nfe_emitida

# class OrderAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Dados da Ordem', {
#             'fields':('sale', 'reference_code', 'internal_code', 'customer')
#             }),
#         ('Preços e Serviços',{
#             'fields': ('price', 'description','description_2')
#         })
#     )
#     list_display=('sale', 'customer', 'price', 'date')

# class SaleAdmin(admin.ModelAdmin):
#     readonly_fields = ('price',)
#     fields=('reference_code', 'customer', 'discount', 'price')
#     list_filter=('price','discount','date')
#     # raw_id_fields = ('customer')
#     list_display = ('id', 'customer', 'date','discount','price','nfe','date' ) #get_total
#     search_fields = ('id', 'customer_first_name')
#     actions = [nfe_nao_emitida,nfe_emitida]
#     # filter_horizontal = ('product',)
#     # autocomplete_fields = ('product',)
    

# class ProductAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Dados do produto :', {
#             'fields':('image','name', 'category', 'description', 'reference_code')
#         } ),
#         ('Dados de preço :', {
#           'fields':('price', 'is_available')  
#         } )
#     )
#     list_filter= ('id', 'category', 'price')
#     list_display = ('id','image', 'name','description','price' ) 
#     search_fields = ('id', 'name', 'reference_code', 'internal_code')
    
    
# # Register your models here.
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Category)
# admin.site.register(Sale, SaleAdmin)
# admin.site.register(SaleItens)
