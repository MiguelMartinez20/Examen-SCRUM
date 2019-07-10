from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Solicitud, Productor, Producto, Pedido, Post
from comercio.forms import RegisterForm, PedidoForm, PostForm
from django.utils import timezone

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
            return render(request, 'comercio/congrats_account.html', {})
        else:
            ctx = {'form':form}
            return render(request, 'comercio/register.html', ctx)

    ctx = {'form':form}
    return render(request, 'comercio/register.html', ctx)

def productor_list(request):
    productores = Productor.objects.all()
    return render(request, 'comercio/products.html', {'productores': productores})

def productor_detail(request, pk):
    productor = get_object_or_404(Productor, pk=pk)
    productos = Producto.objects.filter(productor=pk)
    return render(request, 'comercio/products_detail.html', {'productor': productor, 'productos':productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion = form.cleaned_data['direccion']
            detalle = producto.detalle
            email = form.cleaned_data['email']

            p = Pedido.objects.create(nombre = nombre, apellido = apellido, direccion = direccion, detalle = detalle, email = email)
            p.save()
            return render(request, 'comercio/congrats.html', {})
        else:
            ctx = {'producto': producto, 'form':form}
            return render(request, 'comercio/products_compra.html', ctx)

    ctx = {'producto': producto, 'form':form}
    return render(request, 'comercio/products_compra.html', ctx)

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'comercio/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("http://scrumexamen.pythonanywhere.com/post/")
    else:
        form = PostForm()
    return render(request, 'comercio/post_edit.html', {'form': form})








