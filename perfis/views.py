import copy

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from perfis.forms import PerfilForm, UserForm
from perfis.models import Perfil

# Create your views here.


class BasePerfil(View):
    templane_name = "perfis/criar.html"

    def setup(self, request, *args, **kwargs) -> None:
        super().setup(request, *args, **kwargs)
        usuario = self.request.user
        self.carrinho = copy.deepcopy(self.request.session.get("carrinho", {}))
        self.perfil = None
        if usuario.is_authenticated:
            self.perfil = Perfil.objects.filter(usuario=usuario).first()
            self.context = {
                "userform": UserForm(
                    data=self.request.POST or None,
                    usuario=usuario,
                    instance=usuario,
                ),
                "perfilform": PerfilForm(
                    data=self.request.POST or None, instance=self.perfil
                ),
            }
            self.templane_name = "perfis/atualizar.html"
        else:
            self.context = {
                "userform": UserForm(data=self.request.POST or None),
                "perfilform": PerfilForm(data=self.request.POST or None),
            }

        self.user_form = self.context["userform"]
        self.perfil_form = self.context["perfilform"]

        self.render = render(self.request, self.templane_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class PerfilCriarView(BasePerfil):
    def post(self, *args, **kwargs):

        if not self.user_form.is_valid() or not self.perfil_form.is_valid():
            self.render

        username = self.user_form.cleaned_data.get("username")
        password = self.user_form.cleaned_data.get("password")
        email = self.user_form.cleaned_data.get("email")
        first_name = self.user_form.cleaned_data.get("first_name")
        last_name = self.user_form.cleaned_data.get("last_name")
        # Usuario Logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)

            if password:
                usuario.set_password(password)
            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

        # Usuario novo (nao logado)
        else:
            pass
            usuario = self.user_form.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfil_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password:
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password,
            )
            if autentica:
                login(self.request, user=usuario)
        self.request.session["carrinho"] = self.carrinho
        self.request.session.save()
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
