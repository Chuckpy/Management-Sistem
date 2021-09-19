from django.http import HttpResponseNotFound

def nfe_emitida(modeladmin, request, queryset) :
    if request.user.has_perm('order.nfe_change'):
        queryset.update(nfe=True)
    else:
        return HttpResponseNotFound('<h1>Permissão negada !</h1>')    
    
nfe_emitida.short_description = 'NF-e Emitida'

def nfe_nao_emitida(modeladmin, request, queryset) :
    if request.user.has_perm('order.nfe_change'):
        queryset.update(nfe=True)
    else:
        return HttpResponseNotFound('<h1>Permissão negada !</h1>')  
    queryset.update(nfe=False)
    
nfe_nao_emitida.short_description = 'NF-e Não Emitida'