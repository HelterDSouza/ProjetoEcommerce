from django.urls import path

from . import views

app_name = "perfis"


urlpatterns = [
    path(
        "",
        views.PerfilCriarView.as_view(),
        name="perfis-criar",
    ),
    path(
        "atualizar/",
        views.PerfilAtualizarView.as_view(),
        name="perfis-atualizar",
    ),
    path(
        "login/",
        views.PerfilLoginView.as_view(),
        name="perfis-login",
    ),
    path(
        "logout/",
        views.PerfilLogoutView.as_view(),
        name="perfis-logout",
    ),
]
