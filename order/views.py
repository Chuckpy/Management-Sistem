from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from user.models import User
from .forms import SaleForm, ProductForm, SaleItemModelForm
from .models import Sale, SaleItem, Product

class SaleListView(ListView):
    
    model = Sale
    paginate_by = 15
    template_name= 'order/sale_list.html'    
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context

class SaleDetailView(DetailView):
    
    model = Sale
    template_name = 'order/sale_detail.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context

class SaleCreateView(View):

    def get(self, request):
        return render(request, 'order/sale_form.html')

    def post(self,request):
        data = {}
        data['form_sale'] = SaleForm()
        data['reference_code'] = request.POST['reference_code']
        data['customer']= request.POST['customer']
        data['discount'] = float(request.POST['discount'])
        data['sale']=request.POST['sale_id']

        if data['sale']:
            sale = Sale.objects.get(id=data['sale'])
            sale.discount = data['discount']
            sale.reference_code = data['reference_code']
            sale.customer = User.objects.get(id=data['customer'])
            sale.save()
        else :
            sale = Sale.objects.create(
                reference_code=data['reference_code'],discount=data['discount'], customer= User.objects.get(id=data['customer'])
            )
            itens = sale.saleitem_set.all()
            data['sale_obj']=sale
            data['itens']=itens

        return render(request, 'order/sale_form.html', data)

class SaleProductAdd(View):

    def get(self, request):
        return render(request, 'order/sale_form.html')


    def post(self, request, sale):
        
        data={}
        
        item = SaleItem.objects.filter(
            product=Product.objects.get(id=request.POST['product_id']),
            sale=Sale.objects.get(id=sale))
                
        if item.exists() :
            data['message']='Item ja incluido no pedido, favor editar'
            item = item[0]
        else :                
            item = SaleItem.objects.create(
                product=Product.objects.get(id=request.POST['product_id']),quantity=request.POST['quantity'],
                discount=request.POST['discount'], sale=Sale.objects.get(id=sale)
            )
            
        data['item']=item
        data['form_item']=ProductForm()
        data['reference_code']=item.sale.reference_code
        data['discount']=item.sale.discount
        data['sale_id']=item.sale.id            
        data['sale_obj']=item.sale
        data['itens']=item.sale.saleitem_set.all()

        return render(request, 'order/sale_form.html', data)

class SaleEditView(View):
    
    def get(self, request, sale):
        data= {}
        sale= Sale.objects.get(id=sale)
        data['form_item']= ProductForm()        
        data['reference_code']=sale.reference_code
        data['discount']=sale.discount
        data['sale_id']=sale.id
        data['sale_obj']=sale
        data['itens']=sale.saleitem_set.all()
        
        return render(request, 'order/sale_edit.html', data)
    
class SaleDeleteView(View):
    
    def get (self, request,sale):
        sale = Sale.objects.get(id=sale)        
        return render(request, 'order/sale_delete.html', {'sale':sale})
        
    def post (self, request,sale):
        sale = Sale.objects.get(id=sale)
        sale.delete()
        return redirect('order:list')

class ProductDeleteView(View):
    
    def get (self, request,item):
        sale_item = SaleItem.objects.get(id=item)
        return render(request, 'order/delete-product.html', {'sale_item':sale_item})
    
    def post (self, request, item):
        sale_item = SaleItem.objects.get(id=item)
        sale_id = sale_item.sale.id
        sale_item.delete()
        request.method= 'GET'
        return redirect('order:edit', sale=sale_id)
    
class EditProductView(View):
    
    def get (self, request, item):
        sale_item = SaleItem.objects.get(id=item)
        form = SaleItemModelForm(instance=sale_item)
        
        return render(request, 'order/edit_product.html', {'sale_item':sale_item, 'form': form})
    
    def post (self, request, item):
        sale_item = SaleItem.objects.get(id=item)
        sale_item.quantity = request.POST['quantity']
        sale_item.discount = request.POST['discount']
        sale_item.sale = Sale.objects.get(id=request.POST['sale'])
        sale_item.product = Product.objects.get(id=request.POST['product'])       
        sale_item.save()
        sale_id= sale_item.sale.id
         
        return redirect('order:edit', sale=sale_id)