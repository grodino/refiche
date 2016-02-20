$(function() {
// Get the sheets
    function getSheets(initialFetch) {
        $.get(
            url = '/app/feed/?initial_fetch=' + initialFetch,
            success = function (response) {
                $('#feed')
                    .html('')
                    .append(response);
            },
            data = 'html'
        );
    }

// Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('top', '0')
        .css('left', '0')
        .css('width', '100%');
    if ($('#left-bar').is(':visible')) {
        $('.nav-icon').addClass('nav-icon-selected');
    }

    if ($('.messages').length === 0) {
        $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');
    } else {
        $('.messages').css('margin-top', $('#banner').height() + 'px');
    }

// Handle the reveal and hide actions for the menu
    $('.nav-icon').click(function () {
        if ($('#left-bar').is(':visible')) {
            $('#left-bar').animate({
                left: '-=24em'
            }, function () {
                $('#left-bar').hide();
            });
            $('#content').animate({
                'margin-left': '1em'
            });

            $('.nav-icon').removeClass('nav-icon-selected');
        } else {
            $('#left-bar').show();
            $('#left-bar').animate({
                display: 'block',
                left: '+=24em'
            });

            if ($(document).width() >= 1100) {
                $('#content').animate({
                    'margin-left': '25em'
                });
            }

            $('.nav-icon').addClass('nav-icon-selected');
        }
    });

    getSheets('true');

    setTimeout(
        function () {
            setInterval(getSheets('true'), 10 * 60 * 1000);
        },
        10 * 60 * 1000
    );
});$(function() {
// Get the sheets
    function getSheets(initialFetch) {
        $.get(
            url = '/app/feed/?initial_fetch=' + initialFetch,
            success = function (response) {
                $('#feed')
                    .html('')
                    .append(response);
            },
            data = 'html'
        );
    }

// Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('top', '0')
        .css('left', '0')
        .css('width', '100%');
    if ($('#left-bar').is(':visible')) {
        $('.nav-icon').addClass('nav-icon-selected');
    }

    if ($('.messages').length === 0) {
        $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');
    } else {
        $('.messages').css('margin-top', $('#banner').height() + 'px');
    }

// Handle the reveal and hide actions for the menu
    $('.nav-icon').click(function () {
        if ($('#left-bar').is(':visible')) {
            $('#left-bar').animate({
                left: '-=24em'
            }, function () {
                $('#left-bar').hide();
            });
            $('#content').animate({
                'margin-left': '1em'
            });

            $('.nav-icon').removeClass('nav-icon-selected');
        } else {
            $('#left-bar').show();
            $('#left-bar').animate({
                display: 'block',
                left: '+=24em'
            });

            if ($(document).width() >= 1100) {
                $('#content').animate({
                    'margin-left': '25em'
                });
            }

            $('.nav-icon').addClass('nav-icon-selected');
        }
    });

    getSheets('true');

    setTimeout(
        function () {
            setInterval(getSheets('true'), 10 * 60 * 1000);
        },
        10 * 60 * 1000
    );
});$(function() {
// Get the sheets
    function getSheets(initialFetch) {
        $.get(
            url = '/app/feed/?initial_fetch=' + initialFetch,
            success = function (response) {
                $('#feed')
                    .html('')
                    .append(response);
            },
            data = 'html'
        );
    }

// Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('top', '0')
        .css('left', '0')
        .css('width', '100%');
    if ($('#left-bar').is(':visible')) {
        $('.nav-icon').addClass('nav-icon-selected');
    }

    if ($('.messages').length === 0) {
        $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');
    } else {
        $('.messages').css('margin-top', $('#banner').height() + 'px');
    }

// Handle the reveal and hide actions for the menu
    $('.nav-icon').click(function () {
        if ($('#left-bar').is(':visible')) {
            $('#left-bar').animate({
                left: '-=24em'
            }, function () {
                $('#left-bar').hide();
            });
            $('#content').animate({
                'margin-left': '1em'
            });

            $('.nav-icon').removeClass('nav-icon-selected');
        } else {
            $('#left-bar').show();
            $('#left-bar').animate({
                display: 'block',
                left: '+=24em'
            });

            if ($(document).width() >= 1100) {
                $('#content').animate({
                    'margin-left': '25em'
                });
            }

            $('.nav-icon').addClass('nav-icon-selected');
        }
    });

    getSheets('true');

    setTimeout(
        function () {
            setInterval(getSheets('true'), 10 * 60 * 1000);
        },
        10 * 60 * 1000
    );
});$(function() {
// Get the sheets
    function getSheets(initialFetch) {
        $.get(
            url = '/app/feed/?initial_fetch=' + initialFetch,
            success = function (response) {
                $('#feed')
                    .html('')
                    .append(response);
            },
            data = 'html'
        );
    }

// Fix the header and move everything according to it
    $('#banner')
        .css('position', 'fixed')
        .css('top', '0')
        .css('left', '0')
        .css('width', '100%');
    if ($('#left-bar').is(':visible')) {
        $('.nav-icon').addClass('nav-icon-selected');
    }

    if ($('.messages').length === 0) {
        $('#main_wrapper').css('margin-top', $('#banner').height() + 'px');
    } else {
        $('.messages').css('margin-top', $('#banner').height() + 'px');
    }

// Handle the reveal and hide actions for the menu
    $('.nav-icon').click(function () {
        if ($('#left-bar').is(':visible')) {
            $('#left-bar').animate({
                left: '-=24em'
            }, function () {
                $('#left-bar').hide();
            });
            $('#content').animate({
                'margin-left': '1em'
            });

            $('.nav-icon').removeClass('nav-icon-selected');
        } else {
            $('#left-bar').show();
            $('#left-bar').animate({
                display: 'block',
                left: '+=24em'
            });

            if ($(document).width() >= 1100) {
                $('#content').animate({
                    'margin-left': '25em'
                });
            }

            $('.nav-icon').addClass('nav-icon-selected');
        }
    });

    getSheets('true');

    setTimeout(
        function () {
            setInterval(getSheets('true'), 10 * 60 * 1000);
        },
        10 * 60 * 1000
    );
});