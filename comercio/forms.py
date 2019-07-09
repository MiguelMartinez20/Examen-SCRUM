from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Pedido

class RegisterForm(forms.Form):

    usuario = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput())
    rut = forms.CharField(label="RUN", widget=forms.TextInput())
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput())
    apellido = forms.CharField(label="Apellido", widget=forms.TextInput())
    email = forms.CharField(label="Correo Electronico", widget=forms.TextInput())
    pyme = forms.CharField(label="PYME", widget=forms.TextInput())
    direccion = forms.CharField(label="Direccion", widget=forms.TextInput())
    photo = forms.ImageField(label="Logotipo PYME")

    password_one = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False), min_length=8)
    password_two = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']

        if(password_one == password_two):
            pass
        else:
            raise forms.ValidationError("Las contraseñas no coinciden")


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'direccion', 'email']