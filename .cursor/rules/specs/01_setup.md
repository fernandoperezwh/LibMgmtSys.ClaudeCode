Crea un proyecto en Django básico para una sistema para administrar libros llamada LibMgmtSys. Debe tener configuración de base de datos SQLite y un endpoint de health. Primero hazlo funcionar localmente, luego dockerízalo.

## PASO 1: Configurar e instalar dependencias

- Trabaja en la carpeta src/ si no existe creala
- Crea un entorno virtual con pipenv con estas dependencias mínimas:
    - Python 3.8
    - Django (LTS)
    - Django-ckeditor (LTS)
    - Pillow (para manejo de imágenes)
- Instala las dependencias en el entorno virtual ya esta pipenv instalado

## PASO 2: Crea la estructura basica de un proyecto de Django
- Ejecuta el comando de django para crear un proyecto usando la carpeta src/

## PASO 3: Verificar funcionamiento local
Verificar que respondan la vista default de django en http://localhost:8000/ 

## PASO 4: Modifica la estructura default

Modifica la conf default de django para que siga la siguiente estructura de carpetas:
```
src/
├── apps/
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── index.html
│
├── pipfile
└── README.md
```

## PASO 5: Crear aplicación Django básica

- Crea la aplicacion "biblioteca" dentro de apps/
- En la aplicacion "src/apps/biblioteca" crea los modelos de Django
- En la aplicacion "src/apps/biblioteca" crea el archivo admin conforme los modelos
- En la aplicacion "src/apps/biblioteca" crea las vistas usando vistas basadas en clases para 
    - Crear, editar, listar y eliminar registros de autores
    - Crear, editar, listar y eliminar registros de libros
    - Crear, editar, listar y eliminar registros de editores
- Las vistas NO deben requerir autenticación (sin LoginRequiredMixin)
- Crear los templates HTML necesarios para todas las vistas usando Bootstrap 5 via CDN
- Aplicar estilos de Bootstrap a todos los campos de formulario usando CSS personalizado
- **Mejorar la UX del campo de fecha**: Convertir el campo de fecha de publicación del libro en un input de tipo `date` (calendario) para evitar errores de formato de fecha y mejorar la experiencia del usuario
- Configurar CKEditor para el campo de descripción de libros:
  - Usar RichTextField en el modelo Libro
  - Configurar CKEDITOR_CONFIGS en settings.py con toolbar básico
  - Cargar archivos CSS y JS de CKEditor en el template base
  - **IMPORTANTE**: Incluir el script de inicialización automática de Django-ckeditor (`ckeditor-init.js`)
  - Configurar archivos estáticos y media para desarrollo
  - Recolectar archivos estáticos con collectstatic
  - **Nota técnica**: Django-ckeditor incluye automáticamente el JavaScript de inicialización en `ckeditor-init.js`, pero este archivo debe ser incluido explícitamente en los templates personalizados (no se carga automáticamente como en el admin de Django)
- Registrar las urls de las vistas para ser accedidas desde el navegador
- Configurar la URL raíz (/) para que redirija a la lista de libros usando una función lambda
- NO crear otras vistas aún


## PASO 6: Verificar funcionamiento local

- Instalar dependencias con poetry creando un venv y ejecutar el proyecto

- Verificar que respondan:
    - http://localhost:8000/ (vista default de django)