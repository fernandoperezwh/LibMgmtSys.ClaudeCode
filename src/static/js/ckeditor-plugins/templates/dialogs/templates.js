CKEDITOR.dialog.add('customTemplatesDialog', function(editor) {
    return {
        title: 'Seleccionar Template',
        minWidth: 500,
        minHeight: 300,
        contents: [
            {
                id: 'tab-templates',
                label: 'Templates',
                elements: [
                    {
                        type: 'html',
                        html: '<div id="templates-loading">Cargando templates...</div><div id="templates-list" style="display:none;"></div>'
                    }
                ]
            }
        ],
        onShow: function() {
            // Cargar templates desde la API
            var dialog = this;
            var loadingDiv = document.getElementById('templates-loading');
            var listDiv = document.getElementById('templates-list');
            
            fetch('/biblioteca/api/templates/')
                .then(response => response.json())
                .then(data => {
                    loadingDiv.style.display = 'none';
                    listDiv.style.display = 'block';
                    
                    var html = '<div class="templates-container">';
                    data.templates.forEach(function(template, index) {
                        html += '<div class="template-item" style="border: 1px solid #ccc; margin: 10px 0; padding: 10px; cursor: pointer;" onclick="selectTemplate(' + index + ')">';
                        html += '<h4>' + template.nombre + '</h4>';
                        if (template.descripcion) {
                            html += '<p style="color: #666; font-size: 12px;">' + template.descripcion + '</p>';
                        }
                        html += '<div style="background: #f5f5f5; padding: 5px; font-size: 11px; max-height: 100px; overflow: auto;">' + template.contenido + '</div>';
                        html += '</div>';
                    });
                    html += '</div>';
                    
                    // Almacenar templates en el diálogo para acceso posterior
                    dialog.templatesData = data.templates;
                    
                    listDiv.innerHTML = html;
                    
                    // Función global para seleccionar template
                    window.selectTemplate = function(index) {
                        var items = document.querySelectorAll('.template-item');
                        items.forEach(item => item.style.backgroundColor = '');
                        event.currentTarget.style.backgroundColor = '#e6f3ff';
                        
                        var selectedTemplate = dialog.templatesData[index];
                        dialog.selectedTemplate = {
                            id: selectedTemplate.id,
                            nombre: selectedTemplate.nombre,
                            contenido: selectedTemplate.contenido
                        };
                    };
                })
                .catch(error => {
                    loadingDiv.innerHTML = 'Error al cargar templates: ' + error;
                });
        },
        buttons: [
            CKEDITOR.dialog.okButton,
            CKEDITOR.dialog.cancelButton
        ],
        onOk: function() {
            if (this.selectedTemplate) {
                editor.insertHtml(this.selectedTemplate.contenido);
            }
        }
    };
});