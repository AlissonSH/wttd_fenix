$(document).ready(function () {
    $("#id_student").select2({
        ajax: {
            delay: 500,
            url: URL_LISTA_STUDENT_AJAX,
            dataType: 'json'
        }
    });
});

