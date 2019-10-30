from django.contrib import admin
from aluguel.models import Aluguel
from cliente.models import Cliente
from endereco.models import Endereco
from itemtema.models import ItemTema
from .models import Tema


admin.site.register(Tema)
admin.site.register(Cliente)
admin.site.register(Aluguel)
admin.site.register(Endereco)
admin.site.register(ItemTema)


# Register your models here.
