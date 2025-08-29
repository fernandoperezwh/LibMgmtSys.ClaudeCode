CKEDITOR.editorConfig = function( config ) {
    // Remover el plugin por defecto de templates y agregar el personalizado
    config.removePlugins = 'templates';
    config.extraPlugins = 'customtemplates';
    
    // Permitir contenido personalizado incluyendo inputs
    config.allowedContent = true;
    config.extraAllowedContent = 'input[type,checked,value,name,id,class,style]';
    
    // Desactivar el filtro automático de contenido
    config.disableAutoInlineEditor = true;
    config.fillEmptyBlocks = false;
    
    // Registrar el plugin personalizado
    CKEDITOR.plugins.addExternal('customtemplates', '/static/js/ckeditor-plugins/templates/', 'plugin.js');
};