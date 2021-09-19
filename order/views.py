from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Sale

class SaleListView(ListView):
    model = Sale
    paginated_by = 10
    template_name= 'order/sale_list.html'
    
    def ger_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context

class SaleDetailView(DetailView):
    
    model = Sale
    template_name= 'order/sale_detail.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context