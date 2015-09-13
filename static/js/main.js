$(function() {
    // Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('width', '100%');
    $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');

    // Dealing with the error and success messages
    $('.success').click(function() {
        $('.success').parent().slideUp('fast');
    });
});
