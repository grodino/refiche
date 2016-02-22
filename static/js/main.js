$(function() {
    // Dealing with the error and success messages
    $('.success').click(function() {
        $('.success').parent().slideUp('fast');
        $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');
    });
});