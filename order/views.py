from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from user.models import User
from .forms import SaleForm,ProductForm
from .models import Sale, SaleItens, Product

class SaleListView(ListView):
    
    model = Sale
    paginate_by = 9
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
            itens = sale.saleitens_set.all()
            data['sale_obj']=sale
            data['itens']=itens

        return render(request, 'order/sale_form.html', data)

class SaleProductAdd(View):

    def get(self, request):
        return render(request, 'order/sale_form.html')


    def post(self, request, sale):
        data={}
        item = SaleItens.objects.create(
            product=Product.objects.get(id=request.POST['product_id']),quantity=request.POST['quantity'],
            discount=request.POST['discount'], sale=Sale.objects.get(id=sale)
        )
        data['item']=item
        data['form_item']=ProductForm()
        data['reference_code']=item.sale.reference_code
        data['discount']=item.sale.discount
        data['sale_id']=item.sale.id
        data['sale_obj']=item.sale
        data['itens']=item.sale.saleitens_set.all()

        return render(request, 'order/sale_form.html', data)
