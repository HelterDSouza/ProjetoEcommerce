from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from produtos.models import Produto, Variacao

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
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            "HTTP_REFERER", reverse("produtos:produtos-lista")
        )
        variacao_id = self.request.GET.get("vid")

        if not variacao_id:
            messages.error(self.request, "Produto não existe")
            return redirect(http_referer)

        variacao = get_object_or_404(Variacao, id=variacao_id)

        if not self.request.session.get("carrinho"):
            self.request.session["carrinho"] = {}
            self.request.session.save()

        carrinho = self.request.session["carrinho"]
        if variacao_id in carrinho:
            # TODO Variação existe no carrinho
            pass
        else:
            # TODO Variação nao existe no carrinho
            pass

        return HttpResponse("teste")


class RemoverCarrinhoView(View):
    pass


class CarrinhoView(View):
    pass


class FinalizarView(View):
    pass
