from django.db import models
from django.db.models import Count, Sum , Max, Avg, Min
import datetime


class SaleManager(models.Manager):
    
    def media(self):
        return self.all().aggregate(Avg('price'))['price__avg']
    def total_month(self):
        now = datetime.datetime.now().month        
        return self.all().filter(date__month=now).aggregate(Sum('price'))['price__sum']
    def media_discount(self):
        return self.all().aggregate(Avg('discount'))['discount__avg']
    def max(self):
        return self.all().aggregate(Max('price'))['price__max']
    def min(self):
        return self.all().aggregate(Min('price'))['price__min']
    def count(self):
        return self.all().count()
    def count_nfe(self):
        return self.filter(nfe=True).aggregate(Count('id'))['id__count']
    def sum_sale(self):
        return self.all().aggregate(Sum('price'))['price__sum']
    def actual_time(self):
        now = datetime.datetime.now()
        return now  
    # TODO :
    # def percent(self):
    #     pass  
    
    # def month_sum(self): #TODO : cada dia somar o valor de cada dia até completar o mês
    #     month = datetime.datetime.now().month
    #     s=self.all().filter(date__month=month)
    #     f=[]
    #     for sale in s:
    #         total = float(sale.price)
    #         f.append(total)
    #     return f
