from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('linea',views.LineaView.as_view(),name='linea'),
    path('marca',views.MarcaView.as_view(),name='marca'),
    path('unidadmedida',views.UnidadMedidaView.as_view(),name='unidadmedida'),
    path('moneda',views.MonedaView.as_view(),name='moneda'),
    path('producto',views.ProductoView.as_view(),name='producto'),
    path('producto/<int:producto_codigo>',views.ProductoView.as_view()),    
    path('ubigeo',views.UbigeoView.as_view(),name='ubigeo'),
    path('tipo_documento',views.Tipo_documentoView.as_view(),name='tipo_documento'),    
    path('clientes',views.ClientesView.as_view(),name='clientes'),    
    path('clientes/<int:clientes_codigo>',views.ClientesView.as_view()),
    path('pedido',views.PedidoView.as_view(),name='pedido'),
    path('pedido/<int:pedido_codigo>',views.PedidoView.as_view()),
    path('pedidodetalle',views.PedidoDetalleView.as_view(),name='pedidodetalle'),
    path('pedidodetalle/<int:pedidodetalle_codigo>',views.PedidoDetalleView.as_view())
]