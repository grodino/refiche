$(function() {
	// Deals with the code inscription button
    $('#student_form_link').click(function() {
        $('#menu').slideUp('fast');
        $('#student_form').slideDown('fast');
    });

    $('#hide_student_form').click(function() {
        $('#menu').slideDown('fast');
        $('#student_form').slideUp('fast');
    });


    //Deals with the code inscription form
    $('#student_registration').submit(function(e) {
    	e.preventDefault();
    	$('#id_code').removeClass('error');

    	$.post(
                '/register/',
                {
                    'code': $('#id_code').val(),
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function(data) {
                    if (data.success === 'true') {
                        alert('ouiiiiiiiiiii'); // TODO: rediriger vers la page d'inscription
                    } else {
                    	$('#id_code').addClass('error');
                    }
                },
                'json'
            );
    }); 

    // Displays if the user can register after he submitted the code

});
