var file_avatar = document.querySelector('#file_avatar'),
    input_file = document.querySelector('#id_sheetFile');

file_avatar.addEventListener('click', function() {
    input_file.click();
}, false);

input_file.addEventListener('change', function() {
    if (input_file.value !== '') {
        file_avatar.setAttribute('value', input_file.value.replace("C:\\fakepath\\", ""));
    } else {
        file_avatar.setAttribute('value', 'Selectionner le fichier');
    }
    
}, false);


var newSheetForm = document.querySelector('#new_sheet_form'),
    userInfos = document.querySelector('#user_infos').cloneNode(true),
    classroomsProfile = document.querySelector('#classroom_profile').cloneNode(true),
    newSheetLink = document.querySelector('#new_sheet_link');

function postNewSheet() {
    if (newSheetForm.style.display == 'block') {
        hideNewSheetForm();
    } else {
        showNewSheetForm();
    }
}

function hideNewSheetForm() {
    newSheetForm.style.display = 'none';
    userInfos.style.display = 'block';
    classroomsProfile.style.display = 'block';
}

function showNewSheetForm() {
    newSheetForm.style.display = 'block';
    alert(userInfos.parentElement);
    classroomsProfile.parentNode.removeChild(classroomsProfile);  

}

function submitForm() {
    var formResponse = new XMLHttpRequest(),
        sheetForm = document.querySelector('#id_sheet_form'),
        sheetFormData = new FormData(sheetForm);
    
    formResponse.open('POST', 'http://refiche.dev:8000/app/upload/');
    formResponse.send(sheetFormData);
    
    formResponse.addEventListener('readystatechange', function() {
        if (formResponse.readyState === formResponse.DONE) {
            if (formResponse.getResponseHeader('Content-type') === 'application/json') {
                alert(formResponse.responseText);
            } else {
                alert('Oh non :( Une erreur est survenue')
            }
        }
    }, false);
}






































