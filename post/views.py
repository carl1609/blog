from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from .models import Publicaciones
from django.contrib.auth.forms import UserCreationForm

class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicaciones
    fields = ['titulo', 'contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ActualizarPublicacion(LoginRequiredMixin, UpdateView):
    model = Publicaciones
    fields = ['titulo', 'contenido']
    template_name = 'actualizar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')

    def get_queryset(self):
        return Publicaciones.objects.filter(autor=self.request.user)
    
class BorrarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicaciones
    template_name = 'borrar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')

    def get_queryset(self):
        return Publicaciones.objects.filter(autor=self.request.user) 


class ListaPublicaciones(ListView):
    model = Publicaciones
    template_name = 'home.html'
    context_object_name = 'publicaciones'
    ordering = ['-fecha']

class DetallePublicacion(DetailView):
    model = Publicaciones
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'

class MisPublicaciones(LoginRequiredMixin, ListView):
    model = Publicaciones
    template_name = 'mis_publicaciones.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        return Publicaciones.objects.filter(autor=self.request.user)

class Resgistro(CreateView):
    template_name='registro.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('login')    

class BuscarPublicaciones(ListView):
    model = Publicaciones
    template_name = 'buscar_publicacion.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        
        titulo = self.request.GET.get('titulo')
        publicaciones=Publicaciones.objects.filter(titulo=titulo)
        return publicaciones