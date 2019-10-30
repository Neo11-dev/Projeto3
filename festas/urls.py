from django.contrib import admin
from django.urls import path
from tema.views import home
from cliente.views import home
from endereco.views import home
from itemtema.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tema/', home),
    path('cliente/', home),
    path('aluguel/', home),
    path('endereco/', home),
    path('itemtema/', home),
]
