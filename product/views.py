from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from order.models import Order
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib import messages

# Create your views here.

# @login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('product:home')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'product/products.html', context)


# @login_required(login_url='user-login')
class ProductDetailView(DetailView):
    
    model = Product
    template_name= 'product/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context

class ProductUpdateView(UpdateView):    
    model = Product
    fields = ['name', 'category','description', 'reference_code', 'price', 'image',]
    template_name_suffix = '_edit'
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Produto atualizado com sucesso.') 
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    # def get_object(self):
    #     return Product.objects.get(pk=self.request.GET.get('pk')) 

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'description', 'reference_code', 'price', 'image']
    
    
# TODO : @login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('product:home')
    context = {
        'item': item
    }
    return render(request, 'product/products_delete.html', context)

def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product:home')
    else:
        form = ProductForm(instance=item)
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'form': form,
        }
    return render(request, 'product/products_edit.html', context)
