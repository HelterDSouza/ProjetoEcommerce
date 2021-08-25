from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView

from .models import Perfil


# Create your views here.
class PerfilCreateView(CreateView):
    pass


# class PerfilCreateView(View):
#     model = Perfil
#     template_name = ".html"


class PerfilUpdateView(UpdateView):
    pass


# class PerfilUpdateView(View):
#     model = Perfil
#     template_name = ".html"


class PerfilLoginView(LoginView):
    pass


# class PerfilLoginView(View):
#     pass


class PerfilLogoutView(LogoutView):
    pass


# class PerfilLogoutView(View):
#     pass
