$(document).ready(function () {
    $("#id_student").select2({
        ajax: {
            delay: 500,
            url: URL_LISTA_STUDENT_AJAX,
            dataType: 'json'
        }
    });
    $("#id_student").on('change', function () {
        getDadosStudent();
    });
});

const getDadosStudent = () => {
    axios.get(URL_DADOS_STUDENT_AXIOS, {
        params: {
            "id": $("#id_student").find('option:selected').val()
        }
    })
    .then((response) => {
        console.log(response)
    })
}
