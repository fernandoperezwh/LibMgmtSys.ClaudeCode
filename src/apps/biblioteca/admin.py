from django.contrib import admin
from .models import Editorial, Autor, Libro


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'pais', 'website']
    list_filter = ['pais', 'estado']
    search_fields = ['nombre', 'ciudad', 'pais']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'email']
    list_filter = ['nombre']
    search_fields = ['nombre', 'apellidos', 'email']
    ordering = ['apellidos', 'nombre']


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'editor', 'fecha_publicacion']
    list_filter = ['editor', 'fecha_publicacion', 'autores']
    search_fields = ['titulo', 'autores__nombre', 'autores__apellidos', 'editor__nombre']
    prepopulated_fields = {'slug': ('titulo',)}
    filter_horizontal = ['autores']
    date_hierarchy = 'fecha_publicacion'
