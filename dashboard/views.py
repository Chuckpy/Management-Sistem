from django.shortcuts import render
from django.views import View
from order.models import Sale, SaleItens
from django.contrib.auth.decorators import login_required


class DashboardView(View):    
    def get(self, request):      
        sale_list = Sale.objects.all() 
        sale_count = sale_list.count()
        sale_average = Sale.objects.media()
        disc_average = Sale.objects.media_discount()
        max_price = Sale.objects.max()
        min_price = Sale.objects.min()
        count_sale = Sale.objects.count()
        count_sale_nfe = Sale.objects.count_nfe()
        total_month = Sale.objects.total_month()
        actual_time = Sale.objects.actual_time()
        # Total preço por data
        total_day = Sale.objects.raw("SELECT id, Sum (price) as p, date, STRFTIME('%%m',date) as month, STRFTIME('%%d',date) as day, STRFTIME('%%Y',date) as year from order_sale GROUP BY year, month, day")        
        # Total itens vendidos por produto
        sale_itens= SaleItens.objects.raw("SELECT itens.id, product_id, name, Sum(quantity) as quantity FROM order_saleitens as itens INNER JOIN product_product as product on itens.product_id = product.id GROUP BY product_id ORDER BY quantity DESC LIMIT 5")
        
   
        return render(request, 'dashboard/index.html', {'average': sale_average, 
                                                        'disc_average': disc_average,
                                                        'min':min_price,
                                                        'max':max_price, 
                                                        'count':count_sale,
                                                        'count_nfe' :count_sale_nfe,
                                                        'total_month': total_month,
                                                        'actual_time': actual_time,                                                        
                                                        'sale_list': sale_list,
                                                        'sale_c' : sale_count,
                                                        'total_day': total_day,
                                                        'sale_list':sale_itens,
                                                        })
    