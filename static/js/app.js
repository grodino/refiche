// Animation to post a new sheet
$(function() {
    // File input button more beautiful
    var file_avatar = document.querySelector('#file_avatar'),
    input_file = document.querySelector('#id_sheetFile');

    file_avatar.addEventListener('click', function() {
        input_file.click();
    }, false);

    input_file.addEventListener('change', function() {
        if (input_file.value !== '') {
            file_avatar.setAttribute('value', input_file.value.replace("C:\\fakepath\\", ""));
        } else {
            file_avatar.setAttribute('value', 'Selectionner le fichier');
        }

    }, false);
    
    // Animation to post a new sheet
    $('#post_new_sheet_link').click(function() {
        $('nav').slideUp('fast');
        $('#new_sheet_form').slideDown('fast');
    });
    
    $('#hide_new_sheet_form').click(function() {
        $('nav').slideDown('fast');
        $('#new_sheet_form').slideUp('fast');
    });
    
    // Dealing with the form
    $('#submit_form').click(function() {
        var formResponse = new XMLHttpRequest(),
        sheetForm = document.querySelector('#id_sheet_form');

        //clean errors
        $('#id_name').removeClass('error');
        $('#id_lesson').removeClass('error');
        $('#file_avatar').removeClass('error');

        // If one of the fields is empty
        if ($('#id_name').val() === '' || $('#id_lesson').val() === '' || $('#id_sheetFile').val() === '') {
            if ($('#id_name').val() === '') {
                $('#id_name').addClass('error');
            }
            if ($('#id_lesson').val() === '') {
                $('#id_lesson').addClass('error');
            }
            if ($('#id_sheetFile').val() === '') {
                $('#file_avatar').addClass('error');
            }
            
            alert('Oops je crois que tu as oublié quelque chose !');
        } else {
            var sheetFormData = new FormData(sheetForm);

            formResponse.open('POST', 'http://refiche.dev:8000/app/upload/');
            formResponse.send(sheetFormData);

            formResponse.addEventListener('readystatechange', function() {
                if (formResponse.readyState === formResponse.DONE) {
                    if (!formResponse.getResponseHeader('Content-type') === 'application/json') {
                        alert('Oh non :( Une erreur est survenue')
                    }

                    var status = $.parseJSON(formResponse.responseText);

                    if (status.sucess) {
                        location.reload();
                    } else {
                        alert('Oh non :( Je crois que j\'ai avalé de travers');
                    }
                }
            }, false);
        }
    });
    
    $('.success').click(function() {
        $('.success').slideUp('fast');
    });
});



































