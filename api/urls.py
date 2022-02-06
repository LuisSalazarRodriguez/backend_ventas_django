from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('linea',views.LineaView.as_view(),name='linea'),
    path('marca',views.MarcaView.as_view(),name='marca'),
    path('unidadmedida',views.UnidadMedidaView.as_view(),name='unidadmedida'),
    path('moneda',views.MonedaView.as_view(),name='moneda'),
    path('producto',views.ProductoView.as_view(),name='producto'),
    path('producto/<int:producto_codigo>',views.ProductoView.as_view())
]