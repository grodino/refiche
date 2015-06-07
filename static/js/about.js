$(function() {
    // make the logo bigger and the link to the home page smaller
    $('header #logo').removeClass('logo');
    $('header a').removeClass('full-container-size').addClass('full-container-width');
    
    var header = $('#miew')
    
    $(window).scroll(function() {
        var windowHeight = document.body.clientHeight,
            currentScroll = document.body.scrollTop || document.documentElement.scrollTop;
        
        header.addClass('fixed');
    });
});































