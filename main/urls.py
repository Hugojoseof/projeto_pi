"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from ecommerce.views import index, produto_criar, admin_pag, produtos,categorias, produto_detalhes, produtos_por_departamento, categoria_detalhes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("produto/", produto_criar, name="produto_criar" ),
    path("admin2/", admin_pag) ,
    path("produtogerais/", produtos, name="produtos" ),
    path("categoriasgerais/", categorias, name="categorias" ),
    path("produto/<int:produto_id>/", produto_detalhes, name="produto_detalhes"),
    path("categoria/<int:categoria_id>/", categoria_detalhes, name="categoria_detalhes"),
    path("departamento/<int:departamento_id>/", produtos_por_departamento, name="produtos_por_departamento"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
