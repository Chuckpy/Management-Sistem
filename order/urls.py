from django.urls import path

from .views import (SaleListView, 
                    SaleDetailView, 
                    SaleCreateView,
                    SaleProductAdd,
                    SaleEditView,
                    SaleDeleteView)

app_name= 'order'

urlpatterns = [
    path('', SaleListView.as_view(), name='list'),
    path('detalhe/<slug:slug>/', SaleDetailView.as_view(), name='detail'),
    path('criar/', SaleCreateView.as_view(), name='new'),
    path('add_product/<int:sale>/', SaleProductAdd.as_view(), name='add_product'),
    path('editar/<int:sale>/', SaleEditView.as_view(), name='edit'),
    path('excluir/<int:sale>/', SaleDeleteView.as_view(), name='delete'),
]