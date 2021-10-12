from django.urls import path

from .views import (SaleListView, 
                    SaleDetailView, 
                    SaleCreateView,
                    SaleProductAdd)

app_name= 'order'

urlpatterns = [
    path('', SaleListView.as_view(), name='list'),
    path('detail/<slug:slug>/', SaleDetailView.as_view(), name='detail'),
    path('criar/', SaleCreateView.as_view(), name='new'),
    path('add_product/<int:sale>/', SaleProductAdd.as_view(), name='add_product'),
]