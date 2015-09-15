$(function() {
    // Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('width', '100%');
    $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');

    // Get the sheets
    $.get(
        url='/app/feed/',
        success=function(response) {
            console.log(response);

            for (sheet in response) {
                $('#feed')
                    .append(response[sheet].name)
                    .append(response[sheet].firstName);
            }
        },
        data='json'
    )
});