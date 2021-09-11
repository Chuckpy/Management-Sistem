def nfe_emitida(modeladmin, request, queryset) :
    queryset.update(nfe=True)
    
nfe_emitida.short_description = 'NF-e Emitida'

def nfe_nao_emitida(modeladmin, request, queryset) :
    queryset.update(nfe=False)
    
nfe_nao_emitida.short_description = 'NF-e Não Emitida'