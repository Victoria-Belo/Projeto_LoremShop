#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Produto

def index(request):
    return render(request, 'index.html')

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    p = Produto.objects.all()
    print(p)
    context = {
        'produtos': p
    }
    return render(request, 'produto.html', context)
























































#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************