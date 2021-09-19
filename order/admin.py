from django.contrib import admin
from .models import Order, Sale, SaleItens
from .actions import nfe_nao_emitida, nfe_emitida

class SaleItemInLine(admin.TabularInline):
    model = SaleItens

class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados da Ordem', {
            'fields':('sale', 'reference_code', 'internal_code', 'customer','slug',)
            }),
        ('Preços e Serviços',{
            'fields': ('price', 'description','description_2',)
        })
    )
    list_display=('sale', 'customer', 'price', 'date')

class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)
    fields=('reference_code', 'customer', 'discount','status', 'price')
    list_filter=('price','discount','date')
    # raw_id_fields = ('customer')
    list_display = ('customer', 'date','discount','price','nfe','date' ) #get_total
    search_fields = ('id', 'customer_first_name')
    actions = [nfe_nao_emitida,nfe_emitida]
    inlines = [SaleItemInLine]
    # filter_horizontal = ('product',)
    autocomplete_fields = ('customer',)

class SaleItensAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'discount')
    search_fields = ('sale', 'product')
    autocomplete_fields = ('sale', 'product')

    
# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleItens, SaleItensAdmin)
