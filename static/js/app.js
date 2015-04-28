var file_avatar = document.querySelector('#file_avatar'),
    input_file = document.querySelector('#id_sheetFile');

file_avatar.addEventListener('click', function() {
    input_file.click();
}, false);

input_file.addEventListener('change', function() {
    if (input_file.value !== '') {
        file_avatar.setAttribute('value', input_file.value);
    } else {
        file_avatar.setAttribute('value', 'Selectionner le fichier');
    }
    
}, false);

