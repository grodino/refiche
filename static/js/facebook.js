$(function() {
    // Prompts the user to log in the app.
    // If the user does it wrong, it tries again
    function facebookLogin(rerequest){
        if (rerequest == false) {
            FB.login(
                function(response) { loginStatusCallback(response); },
                {scope: 'email'}
            );
        } else {
            FB.login(
                function(response) { loginStatusCallback(response); },
                { scope: 'email',
                  auth_type: 'rerequest'}
            );
        }
    }

    // Function made request the server to create a class group
    function createClassGroup(userId) {
        console.log('User id :', userId);

        $.get(
            url = '/facebook/create-group/' + $('#token').val() + '/' + userId,
            success = function(status) {
                if (status.success) {
                    $('#facebook_button').html('Création terminée!');
                    $('#facebook_button').off('click');

                    $('<a href="https://www.facebook.com/groups/' + status.id + '">Voir le groupe</a>').insertAfter($('#facebook_button'));
                } else {
                    alert('Une erreur s\'est produite :/');
                    $('#facebook_button').html('Réessayer');
                }
            },
            dataType = 'json'
        );
    }

    // Function made to check if the user is connected
    // If not, it asks him to do so
    // Then returns the user id
    function loginStatusCallback(response) {
        var userId;
        console.log('Facebook status :', response.status)

        if (response.status === 'connected'){
            userId = response.authResponse.userID;

            createClassGroup(userId);
        } else if (response.status === 'not_authorized'){
            facebookLogin(true); //Because it's a retry
        } else {
            facebookLogin(false);
        }
    }

    $('#facebook_button').click(function(e) {
        console.log('User triggered the facebook button');

        FB.getLoginStatus(function(response) {
            $('#facebook_button').html('Création du groupe ...');
            loginStatusCallback(response);
        });
    });

    $.getScript('//connect.facebook.net/fr_FR/sdk.js', function(){
        FB.init({
          appId: '1423338201308406',
          version: 'v2.3'
        });

        $('#facebook_button').removeAttr('disabled');
    });
});