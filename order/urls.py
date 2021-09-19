from order.models import Sale
from django.urls import path

from .views import SaleListView, SaleDetailView

app_name= 'order'

urlpatterns = [
    path('lista/', SaleListView.as_view(), name='list'),
    path('<slug:slug>/', SaleDetailView.as_view(), name='detail'),
]