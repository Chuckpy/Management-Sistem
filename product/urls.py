from django.urls import path
from . import views
from .views import ProductDetailView, ProductUpdateView, ProductCreateView

app_name = "product"

urlpatterns = [
    path('', views.products, name='home'),
    path('delete/<int:pk>/', views.product_delete,name='delete'),
    path('detalhe/<slug:slug>/', ProductDetailView.as_view(),name='detail'),
    path('update/<slug:slug>/', ProductUpdateView.as_view(),name='update'),
    path('criar/', ProductCreateView.as_view(),name='create'),
]