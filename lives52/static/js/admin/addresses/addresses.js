$(function(){

  function create_or_display_errors($form, data){
    // Create or display erros on form.
    if ('success' in data){
      // Reload page.
      window.location = '.';
    }
    error_clas = 'ui-state-error-text';

    // Remove all errors before new response.
    $form.find($('.'+ error_clas +'')).remove();

    prefix = '#id_';
    // Loop through errors and add them.
    $.each(data, function(name, error){
      $form.find($(prefix + name)).after(
        '<p class="'+ error_clas +'">' + error.join() + '</p>'
      );
    });
  }

  // Add address dialog
  $('.add-address-dialog').dialog({
    autoOpen: false,
    width: 450,
    height: 500,
    draggable: false,
    modal: true,
    resizable: false,
    stack: true,
    buttons: {
      'Add address': function(){
        $form = $('.add-address-form');
        url_to_post = $form.attr('action');
        $.post(url_to_post, $form.serializeArray(), function(data){

          create_or_display_errors($form, data);

        });
      },
      'Cancel': function() {
        $(this).dialog('close');
      },
    }
  });

  // Add note event click
  $('.add-address').click(function(e){
    e.preventDefault();
    $(".add-address-dialog").dialog('open');
  });

});

