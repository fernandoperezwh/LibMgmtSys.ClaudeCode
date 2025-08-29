CKEDITOR.plugins.add('customtemplates', {
    icons: 'customtemplates',
    init: function(editor) {
        // Comando para abrir el diálogo de templates
        editor.addCommand('customTemplatesDialog', new CKEDITOR.dialogCommand('customTemplatesDialog'));
        
        // Botón en la toolbar
        editor.ui.addButton('CustomTemplates', {
            label: 'Insertar Template',
            command: 'customTemplatesDialog',
            toolbar: 'insert',
            icon: this.path + 'icons/customtemplates.png'
        });
        
        // Registrar el diálogo
        CKEDITOR.dialog.add('customTemplatesDialog', this.path + 'dialogs/templates.js');
    }
});