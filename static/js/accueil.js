$(function() {
    function slideBigPictureLeft() {
        $('#big-picture').addClass('slided');

        $('#left-bar')
            .css('background-color', '#3A6BAA')
            .css('background-image', 'none')
            .css('width', '20%')
            .css('display', 'block');

        $('#login').hide();
        $('#menu').removeClass('hidden');

        $('#left-bar header').css('background-color', '#3B6AAA');
        $('#logo_primary').hide();
        $('#logo').show();
    }

    $('#big-picture button').click(slideBigPictureLeft);
    $(window).resize(function () {
        window.location.reload(false);
    })
});