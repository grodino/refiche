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
    userInfos = document.querySelector('#user_infos'),
    classroomsProfile = document.querySelector('#classroom_profile'),
    newSheetLink = document.querySelector('#new_sheet_link');

function postNewSheet() {
    if (newSheetForm.style.display == 'block') {
        hideNewSheetForm()
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
    userInfos.style.display = 'none';
    classroomsProfile.style.display = 'none';
    
    
}