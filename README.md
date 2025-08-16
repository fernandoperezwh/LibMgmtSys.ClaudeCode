# LibMgmtSys

## Descripcion del proyecto

LibMgmtSys es sistema web para administrar libros. Cada libro contiene información basica y de su autor. Es una implementacion minimalista enfocada en la funcionalidad core de administración de existencia de libros.

## Stack tecnologico

### Backend
- Python 3.8 - Lenguaje principal
- Django (LTS) - Framework web
- Django-ckeditor (LTS) - Editor de texto enriquecido para campos de descripción
- Pillow - Manejo de imágenes para portadas de libros
- SQLite - Base de datos relacional
- Docker - Contenedores para despliegue y desarrollo local

### Frontend
- Javascript - Lenguaje principal
- CSS - Estilos
- Bootstrap 5 - Estilos de componente web modernos via CDN
- HTML con el sistema de templates de Django
- CKEditor - Editor de texto enriquecido integrado

## Entidades del sistema

### Editorial
- **id**: Identificador único
- **slug**: URL amigable generada automáticamente desde el nombre
- **nombre**: Nombre de la editorial
- **domicilio**: Dirección física
- **ciudad**: Ciudad donde se ubica
- **estado**: Estado o provincia
- **pais**: País de origen
- **website**: Sitio web (opcional)

### Autor
- **id**: Identificador único
- **nombre**: Nombre del autor
- **apellidos**: Apellidos del autor
- **email**: Correo electrónico de contacto

### Libro
- **id**: Identificador único
- **slug**: URL amigable generada automáticamente desde el título
- **titulo**: Título del libro
- **autores**: Relación muchos a muchos con autores
- **editor**: Relación con la editorial (ForeignKey)
- **fecha_publicacion**: Fecha de publicación (con selector de calendario)
- **portada**: Imagen de portada (opcional, con Pillow)
- **descripcion**: Descripción del libro usando CKEditor (RichTextField)



## Funcionalidades implementadas

### CRUD Operations
- **Crear, editar, listar y eliminar** registros de Editoriales
- **Crear, editar, listar y eliminar** registros de Autores  
- **Crear, editar, listar y eliminar** registros de Libros

### Características técnicas
- **Vistas basadas en clases (CBVs)**: ListView, CreateView, UpdateView, DeleteView, DetailView
- **Sin autenticación requerida**: Las vistas son públicas para facilitar el uso
- **URLs amigables**: Sistema de slugs automáticos para URLs legibles
- **Admin integrado**: Panel de administración completo con Django Admin
- **Responsive design**: Interfaz adaptada a dispositivos móviles con Bootstrap 5

### Mejoras de UX
- **Selector de calendario**: Campo de fecha con input tipo `date` para evitar errores de formato
- **Editor de texto enriquecido**: CKEditor integrado para descripciones de libros
- **Validación de formularios**: Mensajes de error claros y estilos de Bootstrap
- **Navegación intuitiva**: Menú de navegación con iconos y breadcrumbs

## Estructura del proyecto

```
src/
├── apps/
│   └── biblioteca/          # Aplicación principal
│       ├── models.py        # Modelos de datos
│       ├── views.py         # Vistas basadas en clases
│       ├── admin.py         # Configuración del admin
│       ├── urls.py          # URLs de la aplicación
│       └── templates/       # Templates HTML
├── core/                    # Configuración del proyecto
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
├── templates/               # Templates globales
├── static/                  # Archivos estáticos
├── media/                   # Archivos subidos por usuarios
└── manage.py                # Script de gestión de Django
```

## Enfoque del proyecto

El enfoque es mantener la simplicidad y funcionalidad core sin features adicionales complejas, priorizando:
- **Usabilidad**: Interfaz clara e intuitiva
- **Mantenibilidad**: Código limpio y bien estructurado
- **Escalabilidad**: Arquitectura que permite futuras expansiones
- **Rendimiento**: Optimización para operaciones CRUD básicas