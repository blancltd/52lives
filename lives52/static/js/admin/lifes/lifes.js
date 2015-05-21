$(document).ready(function(){

  // Add note dialog
  $('.add-note-dialog').dialog({
    autoOpen: false,
    width: 450,
    height: 360,
    draggable: false,
    modal: true,
    resizable: false,
    stack: true,
    buttons: {
      'Add note': function(){
        $form = $('.add-note-form');
        url_to_post = $form.attr('action');
        $.post(url_to_post, $form.serializeArray(), function(data){

          if ('success' in data){
            // Reload page.
            window.location = '.';
          }
          error_clas = 'ui-state-error-text';

          // Remove all errors before new response.
          $form.find($('.'+ error_clas +'')).remove();

          prefix = '#id_';
          $.each(data, function(name, error){
            $form.find($(prefix + name)).before(
              '<p class="'+ error_clas +'">' + error.join() + '</p>'
            );
          });
        });
      },
      'Cancel': function() {
        $(this).dialog('close');
      },
    }
  });

  // Add note event click
  $('.add-note').click(function(e){
    e.preventDefault();
    $(".add-note-dialog").dialog('open');
  });

});

