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


    // User options
    // Show
    $('#user_infos_content').click(function(){
        $('#user_infos').css('height', $('#user_infos').outerHeight());
        $('#user_infos_content').slideUp('fast');
        $('#user_options').slideDown('fast');
        $('#user_infos').css('border', '1px solid #3A6BAA');
    });

    // Hide
    $('#hide_user_options').click(function(){
        $('#user_infos_content').slideDown('fast');
        $('#user_options').slideUp('fast');
        $('#user_infos').css('border', '');
    });

    // Animation to post a new sheet
    // Show
    $('#post_new_sheet_link').click(function() {
        $('nav').slideUp('fast');
        $('#new_sheet_form').slideDown('fast');
    });

    // Hide
    $('#hide_new_sheet_form').click(function() {
        $('nav').slideDown('fast');
        $('#new_sheet_form').slideUp('fast');
    });

    //Animation for getting a code
    $('#get_code').click(function() {
        $('nav').slideToggle('fast');
        $('#new_code_form').slideToggle('fast');
    });

    // If the value is changed after an error
    $('#id_numberOfStudents').change(function() {
        $('#id_numberOfStudents').removeClass('error');
    });

    // Dealing with the get code form
    $('#submit_new_code_form').click(function() {
        // If the form is not empty
        if ($('#id_numberOfStudents').val() >=1) {
            var request = new FormData($('#submit_new_code_form form')),
                response = new XMLHttpRequest();

            // TODO: Deal with the error I get when I send the form : 403 forbidden (the server side says it's because of the csrf token)
            alert(request);
            // Send the form to the server
            response.open('POST', '/register/get-student-code/');
            response.send(request.toArray());

            // Deal with the response
            response.addEventListener('readystatechange', function() {
                if (response.readyState === response.DONE) {
                    if (!response.getResponseHeader('Content-type') === 'application/json') {
                        alert('Oh non :( Une erreur est survenue')
                    }

                    var status = $.parseJSON(response.responseText);

                    if (status.sucess) {
                        alert(status);
                    } else {
                        alert('Oh non :( Je crois que j\'ai avalé de travers');
                    }
                }
            }, false);

        } else {
            $('#id_numberOfStudents').addClass('error');
        }

    });

    
    // Dealing with the new sheet_form
    $('#submit_new_sheet_form').click(function() {
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
    
    // Reveals informations about a sheet 
    $('.sheet').hover(function () {
        $('.sheet_info', this).show('fast');
    }, function() {
        $('.sheet_info', this).stop(true, false);
        $('.sheet_info', this).hide('fast');
    }).delay(5000);
});



































