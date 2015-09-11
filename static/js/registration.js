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
        var code = $('#id_code').val();

    	$.post(
                '/register/',
                {
                    'code': code,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function(data) {
                    if (data.success === 'true') {
                        location.replace('/register/code/'+code);
                    } else {
                    	$('#id_code').addClass('error');
                    }
                },
                'json'
            );
    });

    // Dealing with the choice to register with facebook or not
    if ($('.registration_form')) {
        $('body').addClass('no-scroll');
        $('body').bind('touchmove', function(e){e.preventDefault()}); // For mobile devices

        $('#content, #banner, footer').addClass('blur');
        $('#registering_method').removeClass('hidden').addClass('full-size-popup');



        $('body').unbind('touchmove');
    }

});
