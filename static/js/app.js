function getFile() {
    document.getElementById('id_sheetFile').click();
    
    if (document.getElementById('id_sheetFile').value != '') {
        document.getElementById('file_avatar').value = document.getElementById('id_sheetFile').value;
    }
}