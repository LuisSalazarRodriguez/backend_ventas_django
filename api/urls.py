from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('linea',views.LineaView.as_view(),name='linea'),
    path('marca',views.MarcaView.as_view(),name='marca')
]