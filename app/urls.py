#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import index, contato, produto, sobre


urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre'),
    path('produto', produto, name='produto_lista'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












































#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************