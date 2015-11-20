$(function() {
// File input button more beautiful
    $('#file_avatar').click(function () {
        $('#id_sheetFile').click();
    });

    $('#id_sheetFile').change(function() {
        if ($('#id_sheetFile').val() !== '') {
           $('#file_avatar').val($('#id_sheetFile').val().substring($('#id_sheetFile').val().lastIndexOf('/') + 1 || $('#id_sheetFile').val().lastIndexOf('\\') + 1));
        } else {
            $('#file_avatar').val('Selectionner le fichier');
        }
    });

    // Add and remove a spinner
    function showSpinner() {
        $('#main_wrapper').addClass('blur');
        $('.spinner').css('display', 'block');
    }

    function hideSpinner() {
        $('#main_wrapper').removeClass('blur');
        $('.spinner').css('display', 'none');
    }

// User options
// Show
    $('#user_infos_content').parent().hover(function () {
        $('#user_infos').css('height', $('#user_infos').outerHeight());

        $('#user_infos_content').slideUp('fast');
        $('#user_options').slideDown('fast');

        $('#user_infos').css('border', '1px solid #3A6BAA');
    }, function () {
        $('#user_infos_content').stop(true, false).slideDown('fast');
        $('#user_options').stop(true, false).slideUp('fast');

        $('#user_infos').css('border', '');

        $('#new_code_form').hide();
        $('#new_code_form_success').hide();
    });

// Animation to post a new sheet
// Show
    $('#post_new_sheet_link').click(function () {
        $('nav').slideUp('fast');
        $('#new_sheet_form').slideDown('fast');
    });

// Hide
    $('#hide_new_sheet_form').click(function () {
        $('nav').slideDown('fast');
        $('#new_sheet_form').slideUp('fast');
    });

    // Animation to post a new link
    $('#post_new_link_link').click(function() {
        $('nav').slideUp('fast');
        $('#new_link_form').slideDown('fast');
    });

    $('#hide_new_link_form').click(function() {
        $('nav').slideDown('fast');
        $('#new_link_form').slideUp('fast');
    });

    // Handeling the link form
    $('#new_link_form').submit(function(e) {
        e.preventDefault();

        $('#id_lesson').removeClass('error');
        $('#id_url').removeClass('error');

        if($('#id_lesson').val() == '' || $('#id_url').val() == '' ) {
            if($('#id_lesson').val() == '') {
                $('#id_lesson').addClass('error');
            } else if($('#id_url').val() == '') {
                $('#id_url').addClass('error');
            }

            alert('Je crois que tu as oublié quelque chose :(')
        } else {
            showSpinner();

            $.post(
            '/app/link/',
            {   'csrfmiddlewaretoken': $('#new_link_form input[name="csrfmiddlewaretoken"]').val(),
                'lesson': $('#id_lesson').val(),
                'url': $('#id_url').val()    },
            function(data) {
                if(data.success == 'true') {
                    location.reload()
                } else {
                    hideSpinner();
                    alert('Une erreur est survenue lors de l\'enregistrement du lien :(')
                }
            },
            'json'
        )
        }
    });

//Animation for getting a code
    $('#get_code').click(function () {
        $('#user_options').slideToggle('fast');

        if ($('#new_code_form_success input').val() === 'NONE') {
            $('#new_code_form').slideToggle('fast');
        } else {
            $('#new_code_form_success').slideToggle('fast');
        }
    });

    $('#hide_new_code_success').click(function () {
        $('#new_code_form_success').slideToggle('fast');
        $('#user_options').slideToggle('fast');
    });

    $('#hide_new_code_form').click(function () {
        $('#user_options').slideToggle('fast');
        $('#new_code_form').slideToggle('fast');
    });

// If the value is changed after an error
    $('#id_numberOfStudents').change(function () {
        $('#id_numberOfStudents').removeClass('error');
    });

// Dealing with the get code form
    $('#new_code_form').submit(function (e) {
        e.preventDefault();

        // If the form is not empty
        if ($('#id_numberOfStudents').val() >= 1) {
            $.post(
                '/register/get-student-code/',
                {
                    'numberOfStudents': $('#id_numberOfStudents').val(),
                    'csrfmiddlewaretoken': $('#new_code_form form input[name="csrfmiddlewaretoken"]').val(),

                },
                function (data) {
                    if (data.success === 'true') {
                        $('#new_code_form').slideToggle('fast');
                        $('#new_code_form_success').slideToggle('fast');

                        $('#new_code_form_success input').val(data.code);
                    }
                },
                'json'
            );
        } else {
            $('#id_numberOfStudents').addClass('error');
            alert('Vous ne pouvez pas inscrire un nombre négatif ou nul d\'élèves :/');
        }

    });


// Dealing with the new sheet_form
    $('#submit_new_sheet_form').click(function () {
        var formResponse = new XMLHttpRequest(),
            sheetForm = document.querySelector('#id_sheet_form');

        showSpinner()

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

            formResponse.open('POST', '/app/upload/');
            formResponse.send(sheetFormData);

            formResponse.addEventListener('readystatechange', function () {
                if (formResponse.readyState === formResponse.DONE) {
                    if (!formResponse.getResponseHeader('Content-type') === 'application/json') {
                        alert('Oh non :( Une erreur est survenue')
                    }

                    var status = JSON.parse(formResponse.responseText);

                    if (status.success) {
                        location.reload();
                    } else {
                        alert('Le fichier est trop gros ou il n\'est pas autorisé :/');
                        hideSpinner()
                    }
                }
            }, false);
        }
    });


// Reveals informations about a lesson
    $('.lesson').hover(function () {
        $('a', this).addClass('revealed');

        $('.name_container', this).slideUp('fast');
        $('.info_container', this).slideDown('fast');
    }, function () {
        $('.name_container', this).stop(true, false);
        $('.name_container', this).slideDown('fast');

        $('.info_container, this').stop(true, false);
        $('.info_container, this').slideUp('fast');

        $('a', this).removeClass('revealed');
    });


// Reveals informations about a sheet and a link
    $('.item').hover(function () {
        $('.info', this).show('fast');
    }, function () {
        $('.info', this).stop(true, false);
        $('.info', this).hide('fast');
    }).delay(5000);

    // Deleting sheet action
    $('.delete_link').click(function (e) {
        e.preventDefault();

        if (confirm('Etes vous sûr(e) de vouloir supprimer ce document ?')) {
            $.get(
                url = $(this).attr('href'),
                success = function () {
                    location.reload();
                },
                dataType = 'json'
            );
        }
    });

    // Handle the filter by chapter in the lesson view
    $('.down-arrow').click(function() {
        if($(this).hasClass('down-arrow-selected')) {
            $(this).removeClass('down-arrow-selected');
            $('#filters').addClass('hidden');
        } else {
            $('.down-arrow').addClass('down-arrow-selected');
            $('#filters').removeClass('hidden');
        }
    });

    // Deal with modifying the user infos
    $('#user_info_display .settings').click(function() {
        $('#user_info_content').slideToggle('fast');
        $('#account_form').slideToggle('fast');

        $('#account_form').submit(function(e) {
            e.preventDefault();

            if ($('id_firstName').val() === '' || $('id_firstName').val() === '' || $('id_password1').val() === '' || $('id_password2').val() === '') {
                if ($('id_firstName').val() === '') {
                    $('id_firstName').addClass('error');
                }
                if ($('id_firstName').val() === '') {
                    $('id_lastName').addClass('error');
                }
                if ($('id_password1').val() === '') {
                    $('id_password1').addClass('error');
                }
                if ($('id_password2').val() === '') {
                    $('id_password2').addClass('error');
                }

                alert('Oops je crois que tu as oublié quelque chose :/');
            } else {
                showSpinner();

                $.post(
                    "/register/change-infos/",
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'firstName': $('#id_firstName').val(),
                        'lastName': $('#id_lastName').val(),
                        'password1': $('#id_password1').val(),
                        'password2': $('#id_password2').val()
                    },
                    function(response) {
                        if (response.success === 'true') {
                            alert('Pour des raisons de sécurité vous allez être déconnecté');
                            location.reload();
                        } else {
                            hideSpinner();
                            alert('Une erreur est survenue :(');
                        }
                    },
                    'json'
                );
            }


        });
    });
});


































