from core.settings import USE_I18N
from django import forms
from django.contrib.auth.models import User

from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil

        exclude = ("usuario",)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False, widget=forms.PasswordInput(), label="Senha"
    )
    password2 = forms.CharField(
        required=False, widget=forms.PasswordInput(), label="Confirmar Senha"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
            "email",
        )

    def __init__(self, usuario=None, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.usuario = usuario

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned_data = self.cleaned_data

        usuario_data = cleaned_data.get("username")
        password_data = cleaned_data.get("password")
        password2_data = cleaned_data.get("password2")
        email_data = cleaned_data.get("email")

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        validation_error_messages = {}

        error_msg_user_exists = "Usuario já existe"
        error_msg_email_exists = "Email já existe"
        error_msg_password_match = "Senhas não conferem"
        error_msg_password_short = "Senha muito curta, minimo 6 caracteres"
        error_msg_required_field = "Este campo é obrigatorio"
        # Usuarios logados
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_messages["username"] = error_msg_user_exists

            if password_data:
                if len(password_data) < 6:
                    validation_error_messages["password"] = error_msg_password_short
                if password_data != password2_data:
                    validation_error_messages["password"] = error_msg_password_match
                    validation_error_messages["password2"] = error_msg_password_match

            if email_db:
                if email_data != email_db.email:
                    validation_error_messages["email"] = error_msg_email_exists
        # Usuarios nao logados, cadastro
        else:
            if usuario_db:
                validation_error_messages["username"] = error_msg_user_exists

            if email_db:
                validation_error_messages["email"] = error_msg_email_exists

            if not password_data:
                validation_error_messages["password"] = error_msg_required_field

            if not password2_data:
                validation_error_messages["password2"] = error_msg_required_field

            if len(password_data) < 6:

                validation_error_messages["password"] = error_msg_password_short

            if password_data != password2_data:
                validation_error_messages["password"] = error_msg_password_match
                validation_error_messages["password2"] = error_msg_password_match

        if validation_error_messages:
            raise (forms.ValidationError(validation_error_messages))
