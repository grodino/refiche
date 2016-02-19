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

    function login_facebook(e) {
        e.preventDefault();
        var redirect_uri = 'http://refiche.dev:8000/facebook/login/';

        window.open(
            'https://www.facebook.com/dialog/oauth?client_id=413837768813785&scope=email&response_type=code&redirect_uri=' + redirect_uri,
            '_top'
        );
    }


    /* ---------------------------------------------------------------------
     * EVENTS LISTENERS
     * ---------------------------------------------------------------------*/
    $('#big-picture button').click(slideBigPictureLeft);

    $(window).resize(function () {
        window.location.reload(false);
    });

    $('#facebook_login').click(login_facebook)
});