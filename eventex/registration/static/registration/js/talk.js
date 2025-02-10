$(document).ready(function () {
    $("#id_itenstalk_set-0-talk").on('change', function () {
        getDadosTalk();
    });
})

const getDadosTalk = () => {
    const id_talk = $('#id_itenstalk_set-0-talk').find('option:selected').val();
    if (!id_talk) {
        $("#id_itenstalk_set-0-name_speaker").val("").prop("readonly", false).removeClass("active-readonly").trigger('input');
        $("#id_itenstalk_set-0-start_time").val("").prop("readonly", false).removeClass("active-readonly").trigger('input');
        return;
    }

    axios.get(URL_DADOS_TALK_AXIOS, {
        params: {
            'id': id_talk
        }
    })
    .then((response) => {
        $("#id_itenstalk_set-0-name_speaker").val(response.data.speaker).prop("readonly", true).addClass("active-readonly").trigger('input');
        $("#id_itenstalk_set-0-start_time").val(response.data.start).prop("readonly", true).addClass("active-readonly").trigger('input');
    })
    .catch((error) => {
        console.log("Erro ao carregar a palestra." + error);
    })
}
