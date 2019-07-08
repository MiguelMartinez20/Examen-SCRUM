from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.register, name='register'),
    path('productores/', views.productor_list, name='productor_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)