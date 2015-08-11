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

    	$.post(
                '/register/',
                {
                    'code': $('#id_code').val(),
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),

                },
                function(data) {
                    if (data.success === 'true') {
                        alert('ouiiiiiiiiiii');
                    } else {
                    	alert('nooooooooon');
                    }
                },
                'json'
            );
    }); 

    // Displays if the user can register after he submitted the code

});
