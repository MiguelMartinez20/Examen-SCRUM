from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.register, name='register'),
    path('productores/', views.productor_list, name='productor_list'),
    path('productores/<int:pk>/', views.productor_detail, name='productor_detail'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('post/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)