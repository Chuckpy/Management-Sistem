from django.shortcuts import render
from django.views import View
from order.models import Sale


class DashboardView(View):
    def get(self, request):
                    
        sale_average = Sale.objects.media()
        disc_average = Sale.objects.media_discount()
        max_price = Sale.objects.max()
        min_price = Sale.objects.min()
        count_sale = Sale.objects.count()
        count_sale_nfe = Sale.objects.count_nfe()
        total_month = Sale.objects.total_month()
        actual_time = Sale.objects.actual_time()
        
        labels = ['Setembro']
        data = [float(total_month)]
        
        return render(request, 'dashboard/index.html', {'average': sale_average, 
                                                        'disc_average': disc_average,
                                                        'min':min_price,
                                                        'max':max_price, 
                                                        'count':count_sale,
                                                        'count_nfe' :count_sale_nfe,
                                                        'total_month': total_month,
                                                        'actual_time': actual_time,
                                                        'data': data,
                                                        'labels': labels,
                                                        
                                                        })
    