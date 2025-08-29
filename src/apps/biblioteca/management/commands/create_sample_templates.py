from django.core.management.base import BaseCommand
from apps.biblioteca.models import DescripcionTemplate


class Command(BaseCommand):
    help = 'Crea templates de ejemplo con checkboxes para el CKEditor'

    def handle(self, *args, **options):
        templates = [
            {
                'nombre': 'Características del Libro',
                'descripcion': 'Template para destacar características especiales del libro',
                'contenido': '''<h3>✨ Características especiales:</h3>
<p><input type="checkbox" /> Tapa dura</p>
<p><input type="checkbox" /> Páginas ilustradas a color</p>
<p><input type="checkbox" /> Edición limitada</p>
<p><input type="checkbox" /> Incluye prólogo del autor</p>
<p><input type="checkbox" /> Formato de bolsillo</p>
<br>
<p><strong>Observaciones adicionales:</strong></p>
<p>[Escribir observaciones aquí]</p>'''
            },
            {
                'nombre': 'Lista de Géneros',
                'descripcion': 'Template para categorizar el libro por géneros',
                'contenido': '''<h3>📚 Géneros literarios:</h3>
<p><input type="checkbox" /> Ficción</p>
<p><input type="checkbox" /> No ficción</p>
<p><input type="checkbox" /> Biografía</p>
<p><input type="checkbox" /> Historia</p>
<p><input type="checkbox" /> Ciencia ficción</p>
<p><input type="checkbox" /> Fantasía</p>
<p><input type="checkbox" /> Romance</p>
<p><input type="checkbox" /> Misterio/Thriller</p>
<p><input type="checkbox" /> Ensayo</p>
<p><input type="checkbox" /> Poesía</p>
<br>
<p><strong>Subgénero específico:</strong> [Especificar]</p>'''
            },
            {
                'nombre': 'Estado del Ejemplar',
                'descripcion': 'Template para evaluar el estado físico del libro',
                'contenido': '''<h3>📖 Estado del ejemplar:</h3>
<p><input type="checkbox" /> Nuevo</p>
<p><input type="checkbox" /> Como nuevo</p>
<p><input type="checkbox" /> Muy bueno</p>
<p><input type="checkbox" /> Bueno</p>
<p><input type="checkbox" /> Regular</p>
<br>
<h4>Detalles específicos:</h4>
<p><input type="checkbox" /> Páginas amarillentas</p>
<p><input type="checkbox" /> Marcas de uso menores</p>
<p><input type="checkbox" /> Anotaciones a lápiz</p>
<p><input type="checkbox" /> Cubierta desgastada</p>
<p><input type="checkbox" /> Páginas sueltas</p>
<br>
<p><strong>Notas adicionales:</strong></p>
<p>[Describir cualquier detalle relevante sobre el estado]</p>'''
            },
            {
                'nombre': 'Recomendaciones',
                'descripcion': 'Template para agregar recomendaciones y público objetivo',
                'contenido': '''<h3>🎯 Recomendado para:</h3>
<p><input type="checkbox" /> Lectores principiantes</p>
<p><input type="checkbox" /> Lectores avanzados</p>
<p><input type="checkbox" /> Estudiantes</p>
<p><input type="checkbox" /> Profesionales del área</p>
<p><input type="checkbox" /> Público general</p>
<br>
<h4>Edad recomendada:</h4>
<p><input type="checkbox" /> Infantil (0-12 años)</p>
<p><input type="checkbox" /> Juvenil (13-17 años)</p>
<p><input type="checkbox" /> Adulto (18+ años)</p>
<p><input type="checkbox" /> Toda la familia</p>
<br>
<p><strong>¿Por qué recomendarías este libro?</strong></p>
<p>[Escribir razones para la recomendación]</p>'''
            }
        ]

        for template_data in templates:
            template, created = DescripcionTemplate.objects.get_or_create(
                nombre=template_data['nombre'],
                defaults=template_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Template "{template.nombre}" creado exitosamente.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Template "{template.nombre}" ya existe.')
                )

        self.stdout.write(
            self.style.SUCCESS('¡Templates de ejemplo creados exitosamente!')
        )