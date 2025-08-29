from django.core.management.base import BaseCommand
from apps.biblioteca.models import DescripcionTemplate


class Command(BaseCommand):
    help = 'Crea templates con listas de pasos y checkboxes'

    def handle(self, *args, **options):
        templates = [
            {
                'nombre': 'Proceso de Catalogación',
                'descripcion': 'Lista de pasos para catalogar correctamente un libro',
                'contenido': '''<h3>📚 Proceso de Catalogación del Libro</h3>
<p><strong>Sigue estos pasos para catalogar correctamente:</strong></p>
<ol>
    <li><input type="checkbox" /> Revisar la portada y contraportada del libro</li>
    <li><input type="checkbox" /> Verificar información del autor en fuentes confiables</li>
    <li><input type="checkbox" /> Confirmar datos de la editorial y fecha de publicación</li>
    <li><input type="checkbox" /> Asignar categorías y géneros apropiados</li>
    <li><input type="checkbox" /> Revisar el ISBN y código de barras</li>
    <li><input type="checkbox" /> Tomar fotografías de la portada en alta calidad</li>
    <li><input type="checkbox" /> Escribir resumen o sinopsis del contenido</li>
    <li><input type="checkbox" /> Verificar duplicados en la base de datos</li>
    <li><input type="checkbox" /> Guardar registro completo en el sistema</li>
    <li><input type="checkbox" /> Imprimir etiqueta de identificación (opcional)</li>
</ol>
<p><strong>Notas adicionales:</strong></p>
<p>[Agregar observaciones específicas sobre este libro]</p>'''
            },
            {
                'nombre': 'Evaluación de Estado Físico',
                'descripcion': 'Pasos detallados para evaluar el estado físico de un libro',
                'contenido': '''<h3>🔍 Evaluación Detallada del Estado Físico</h3>
<p><strong>Revisa cada aspecto siguiendo este orden:</strong></p>
<ol>
    <li><input type="checkbox" /> <strong>Cubierta frontal:</strong> Verificar daños, manchas o desgaste</li>
    <li><input type="checkbox" /> <strong>Lomo del libro:</strong> Revisar integridad y legibilidad del texto</li>
    <li><input type="checkbox" /> <strong>Cubierta posterior:</strong> Inspeccionar estado general</li>
    <li><input type="checkbox" /> <strong>Páginas interiores:</strong> Contar y verificar completitud</li>
    <li><input type="checkbox" /> <strong>Encuadernación:</strong> Probar flexibilidad sin forzar</li>
    <li><input type="checkbox" /> <strong>Manchas o marcas:</strong> Documentar cualquier anotación</li>
    <li><input type="checkbox" /> <strong>Olor y humedad:</strong> Verificar ausencia de moho</li>
    <li><input type="checkbox" /> <strong>Páginas sueltas:</strong> Identificar hojas desprendidas</li>
    <li><input type="checkbox" /> <strong>Calidad del papel:</strong> Evaluar amarillamiento o fragilidad</li>
    <li><input type="checkbox" /> <strong>Clasificación final:</strong> Asignar estado según evaluación</li>
</ol>
<p><strong>Resultado de la evaluación:</strong></p>
<p>Estado asignado: _______________</p>
<p>Observaciones especiales: [Detallar hallazgos importantes]</p>'''
            },
            {
                'nombre': 'Preparación para Préstamo',
                'descripcion': 'Lista de verificación antes de prestar un libro',
                'contenido': '''<h3>📋 Preparación para Préstamo de Libro</h3>
<p><strong>Completar antes de entregar al usuario:</strong></p>
<ol>
    <li><input type="checkbox" /> <strong>Verificar disponibilidad:</strong> Confirmar que no está reservado</li>
    <li><input type="checkbox" /> <strong>Revisar estado actual:</strong> Documentar condición antes del préstamo</li>
    <li><input type="checkbox" /> <strong>Validar datos del usuario:</strong> Confirmar identificación y registro activo</li>
    <li><input type="checkbox" /> <strong>Consultar historial:</strong> Revisar préstamos anteriores y retrasos</li>
    <li><input type="checkbox" /> <strong>Establecer fecha de devolución:</strong> Calcular según políticas de la biblioteca</li>
    <li><input type="checkbox" /> <strong>Informar condiciones:</strong> Explicar responsabilidades del préstamo</li>
    <li><input type="checkbox" /> <strong>Registrar transacción:</strong> Actualizar sistema con datos del préstamo</li>
    <li><input type="checkbox" /> <strong>Entregar comprobante:</strong> Proporcionar recibo o recordatorio</li>
    <li><input type="checkbox" /> <strong>Programar recordatorio:</strong> Configurar alerta antes del vencimiento</li>
    <li><input type="checkbox" /> <strong>Documentar en bitácora:</strong> Anotar préstamo en registro físico</li>
</ol>
<p><strong>Información del préstamo:</strong></p>
<p>Usuario: _______________</p>
<p>Fecha de préstamo: _______________</p>
<p>Fecha de devolución: _______________</p>
<p>Observaciones: [Notas especiales sobre este préstamo]</p>'''
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
            self.style.SUCCESS('¡Templates de pasos con checkboxes creados exitosamente!')
        )