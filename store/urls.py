from django.urls import path
from . import views

urlpatterns = [
    path('exit/', views.exit, name='exit'),
    path('', views.index, name='index1'),
    path('index/', views.index, name='index'),
    path('tienda/', views.tienda, name='tienda'),
    path('descuento/', views.descuento, name='descuentos'),
    path('evento/', views.evento, name='eventos'),
    path('contacto/', views.contacto, name='contacto'),
    path('search_results/', views.search_results, name='search_results'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/informacion-basica/', views.info, name='informacion_basica'),
    #path('perfil/facturacion/', billing_view, name='facturacion'),
    path('perfil/configuracion/', views.configuracion, name='configuracion'),
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/<int:id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('facturacion/', views.facturacion, name='generar_factura'),
    path('facturas/', views.facturas, name='facturas'),
]