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
        produto: Produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ""
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if variacao.estoque < 1:
            messages.error(self.request, "Estoque insuficiente")
            return redirect(http_referer)

        if not self.request.session.get("carrinho"):
            self.request.session["carrinho"] = {}
            self.request.session.save()

        carrinho = self.request.session["carrinho"]
        if variacao_id in carrinho:
            # TODO Variação existe no carrinho
            pass
        else:
            carrinho[variacao_id] = {
                "produto_id": produto_id,
                "produto_nome": produto_nome,
                "variacao_nome": variacao_nome,
                "variacao_id": variacao_id,
                "preco_unitario": preco_unitario,
                "variacao_id": variacao_id,
                "preco_unitario_promocional": preco_unitario_promocional,
                "quantidade": quantidade,
                "slug": slug,
                "imagem": imagem,
            }
        self.request.session.save()
        return HttpResponse("teste")


class RemoverCarrinhoView(View):
    pass


class CarrinhoView(View):
    pass


class FinalizarView(View):
    pass
