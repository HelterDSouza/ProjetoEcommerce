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
        self.perfil = None
        if usuario.is_authenticated:
            self.perfil = Perfil.objects.filter(usuario=usuario).first()
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

        self.user_form = self.context["userform"]
        self.perfil_form = self.context["perfilform"]
        self.render = render(self.request, self.templane_name, self.context)
        return self.render

    def get(self, *args, **kwargs):
        return self.render


class PerfilCriarView(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.user_form.is_valid() or not self.perfil_form.is_valid():
            self.render

        usuario = self.user_form.cleaned_data.get("username")
        password = self.user_form.cleaned_data.get("password")
        # Usuario Logado
        if self.request.user.is_authenticated:
            pass
        # Usuario novo (nao logado)
        else:
            usuario = self.user_form.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfil_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
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
