from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from .models import Editorial, Autor, Libro, DescripcionTemplate


# Vistas para Editorial
class EditorialListView(ListView):
    model = Editorial
    template_name = 'biblioteca/editorial_list.html'
    context_object_name = 'editoriales'
    ordering = ['nombre']


class EditorialCreateView(CreateView):
    model = Editorial
    template_name = 'biblioteca/editorial_form.html'
    fields = ['nombre', 'domicilio', 'ciudad', 'estado', 'pais', 'website']
    success_url = reverse_lazy('biblioteca:editorial-list')


class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = 'biblioteca/editorial_form.html'
    fields = ['nombre', 'domicilio', 'ciudad', 'estado', 'pais', 'website']
    success_url = reverse_lazy('biblioteca:editorial-list')


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'biblioteca/editorial_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:editorial-list')


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'biblioteca/editorial_detail.html'


# Vistas para Autor
class AutorListView(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'
    context_object_name = 'autores'
    ordering = ['apellidos', 'nombre']


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'biblioteca/autor_form.html'
    fields = ['nombre', 'apellidos', 'email']
    success_url = reverse_lazy('biblioteca:autor-list')


class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'biblioteca/autor_form.html'
    fields = ['nombre', 'apellidos', 'email']
    success_url = reverse_lazy('biblioteca:autor-list')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:autor-list')


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'


# Vistas para Libro
class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'
    context_object_name = 'libros'
    ordering = ['titulo']


class LibroCreateView(CreateView):
    model = Libro
    template_name = 'biblioteca/libro_form.html'
    fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada', 'descripcion']
    success_url = reverse_lazy('biblioteca:libro-list')


class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'biblioteca/libro_form.html'
    fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada', 'descripcion']
    success_url = reverse_lazy('biblioteca:libro-list')


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:libro-list')


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'biblioteca/libro_detail.html'


# Vista API para Templates
class TemplatesAPIView(View):
    def get(self, request, *args, **kwargs):
        templates = DescripcionTemplate.objects.filter(activo=True).values(
            'id', 'nombre', 'contenido', 'descripcion'
        )
        return JsonResponse({
            'templates': list(templates)
        })
