$(function() {
    // make the logo bigger and the link to the home page smaller
    $('header #logo').removeClass('logo');
    $('header a').removeClass('full-container-size');
    
    var headerInitialHeight = $('header').height(),
        logoInitialHeight = $('#logo').height();
    
    $(window).scroll(function() {
        var windowHeight = $(window).height(),
            currentScroll = $(window).scrollTop();
        
        console.log($('#catchphrase').height());
        
        if (headerInitialHeight-currentScroll >= 170){ // Big header
            $('header').height(headerInitialHeight-currentScroll);
            $('header a').css('background-color', 'rgba(58, 107, 170, 0.38)');
            
            $('#catchphrase').show();
            $('header img').removeClass('img-fixed');
        } else { //Small header
            $('header a').css('background-color', '#3A6BAA');
            
            $('#catchphrase').hide();            
            $('header img').addClass('img-fixed');
            $('header').height($('header img').height()+10);
        }        
    });
});































