$(document).ready(function () {
    $("#id_itenscourse_set-0-course").on('change', function () {
        getDadosCourse();
    });
})


const getDadosCourse = () => {
    const id_course = $('#id_itenscourse_set-0-course').find('option:selected').val();
    if (!id_course) {
        $('#id_itenscourse_set-0-name_speaker').val("").prop("readonly", false).removeClass("active-readonly").trigger("input");
        $('#id_itenscourse_set-0-start_time').val("").prop("readonly", false).removeClass("active-readonly").trigger("input");
        return;
    }

    axios.get(URL_DADOS_COURSE_AXIOS, {
        params: {
            'id': id_course
        }
    })
    .then((response) => {
        $("#id_itenscourse_set-0-name_speaker").val(response.data.speaker).prop("readonly", false).addClass("active-readonly").trigger("input");
        $("#id_itenscourse_set-0-start_time").val(response.data.start).prop("readonly", false).addClass("active-readonly").trigger("input");
    })
    .catch((error) => {
        console.log("Erro ao carregar o curso." + error);
    })
}
