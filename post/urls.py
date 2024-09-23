from django.urls import path
from .views import CrearPublicacion, ActualizarPublicacion, BorrarPublicacion,ListaPublicaciones,DetallePublicacion,MisPublicaciones,Resgistro,BuscarPublicaciones

urlpatterns = [
    path('crear/', CrearPublicacion.as_view(), name='crear_publicacion'),
    path('actualizar/<int:pk>/', ActualizarPublicacion.as_view(), name='actualizar_publicacion'),
    path('borrar/<int:pk>/', BorrarPublicacion.as_view(), name='borrar_publicacion'),
    path('', ListaPublicaciones.as_view(),name='home'),
    path('detalle_publicacion/<int:pk>/',DetallePublicacion.as_view(),name='detalle_publicacion'),
    path('mis_publicaciones/', MisPublicaciones.as_view(),name='mis_publicaciones'),
    path('lista_publicaciones', ListaPublicaciones.as_view(),name='lista_publicaciones'),
    path('registro/', Resgistro.as_view(),name='registro'),
    path('buscar_publicaciones',BuscarPublicaciones.as_view(),name='buscar_publicaciones')

]
