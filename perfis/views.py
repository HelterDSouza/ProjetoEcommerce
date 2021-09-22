from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic.base import View

from perfis.forms import PerfilForm, UserForm
from perfis.models import Perfil

# Create your views here.


class BasePerfil(View):
    templane_name = "perfis/criar.html"

    def setup(self, request, *args, **kwargs) -> None:
        super().setup(request, *args, **kwargs)

        usuario = self.request.user
        if usuario.is_authenticated:

            self.context = {
                "userform": UserForm(
                    data=self.request.POST or None,
                    usuario=usuario,
                    instance=usuario,
                ),
                "perfilform": PerfilForm(data=self.request.POST or None),
            }
        else:
            self.context = {
                "userform": UserForm(data=self.request.POST or None),
                "perfilform": PerfilForm(data=self.request.POST or None),
            }

        self.render = render(self.request, self.templane_name, self.context)
        return self.render

    def get(self, *args, **kwargs):
        return self.render


class PerfilCriarView(BasePerfil):
    def post(self, *args, **kwargs):
        return self.render


class PerfilAtualizarView(BasePerfil):
    def post(self, *args, **kwargs):
        return self.render


class PerfilLoginView(LoginView):
    pass


# class PerfilLoginView(View):
#     pass


class PerfilLogoutView(LogoutView):
    pass


# class PerfilLogoutView(View):
#     pass
