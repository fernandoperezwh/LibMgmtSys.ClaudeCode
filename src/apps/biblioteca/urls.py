from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    # URLs para Editorial
    path('editoriales/', views.EditorialListView.as_view(), name='editorial-list'),
    path('editoriales/crear/', views.EditorialCreateView.as_view(), name='editorial-create'),
    path('editoriales/<int:pk>/', views.EditorialDetailView.as_view(), name='editorial-detail'),
    path('editoriales/<int:pk>/editar/', views.EditorialUpdateView.as_view(), name='editorial-update'),
    path('editoriales/<int:pk>/eliminar/', views.EditorialDeleteView.as_view(), name='editorial-delete'),
    
    # URLs para Autor
    path('autores/', views.AutorListView.as_view(), name='autor-list'),
    path('autores/crear/', views.AutorCreateView.as_view(), name='autor-create'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor-update'),
    path('autores/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='autor-delete'),
    
    # URLs para Libro
    path('libros/', views.LibroListView.as_view(), name='libro-list'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='libro-create'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro-detail'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro-update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro-delete'),
    
    # API para Templates
    path('api/templates/', views.TemplatesAPIView.as_view(), name='templates-api'),
]
