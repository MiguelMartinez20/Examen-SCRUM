from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Solicitud, Productor
from comercio.forms import RegisterForm
# Create your views here.

def home(request):
    return render(request, 'comercio/index.html', {})

#def register(request):
#    return render(request, 'comercio/register.html', {})

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']

            rut = form.cleaned_data['rut']
            pyme = form.cleaned_data['pyme']
            direccion = form.cleaned_data['direccion']
            photo = form.cleaned_data['photo']

            u = User.objects.create_user(username=usuario,first_name=nombre,last_name=apellido, email=email, password=password_one, is_staff=True)
            u.save()

            s = Solicitud.objects.create(rut = rut, nombre = nombre, apellido = apellido, direccion = direccion, pyme = pyme, email = email, photo = photo)
            s.save()
            return render(request, 'comercio/index.html', {})
        else:
            ctx = {'form':form}
            return render(request, 'comercio/register.html', ctx)

    ctx = {'form':form}
    return render(request, 'comercio/register.html', ctx)

def productor_list(request):
    productores = Productor.objects.all()
    return render(request, 'comercio/products.html', {'productores': productores})