from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Editoriales"


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    class Meta:
        verbose_name_plural = "Autores"


class DescripcionTemplate(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del template")
    contenido = models.TextField(verbose_name="Contenido HTML", help_text="HTML del template con checkboxes u otros elementos")
    descripcion = models.TextField(blank=True, verbose_name="Descripción", help_text="Descripción opcional del template")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Template de Descripción"
        verbose_name_plural = "Templates de Descripción"
        ordering = ['nombre']


class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autores = models.ManyToManyField(Autor, related_name='libros')
    editor = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    descripcion = RichTextField(config_name='libro_templates')
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Libros"
