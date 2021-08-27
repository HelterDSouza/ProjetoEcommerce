from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from produtos.models import Produto

# Create your views here.


class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produtos_lista.html"
    context_object_name = "produtos"
    paginate_by = 10


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = "produtos/produtos_detalhe.html"
    context_object_name = "produto"
    slug_url_kwarg = "slug"


class AddCarrinhoView(View):
    pass


class RemoverCarrinhoView(View):
    pass


class CarrinhoView(View):
    pass


class FinalizarView(View):
    pass
