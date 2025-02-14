document.addEventListener('DOMContentLoaded', () => {
    const itensTalk = document.querySelector("#id_itenstalk_set-0-talk")

    $(itensTalk).on('change', async function() {
        await getDadosTalk();
    });
});

async function getDadosTalk() {
    const idTalk = document.querySelector("#id_itenstalk_set-0-talk")?.value;

    if (!idTalk) {
        cleanFields();
        return
    }
    try {
        const response = await axios.get(URL_DADOS_TALK_AXIOS, {
            params: {
                id: idTalk,
            }
        });

        const {start, speaker} = response.data
        const talk_name_speaker = document.getElementById("id_itenstalk_set-0-name_speaker");
        const talk_start_time = document.getElementById("id_itenstalk_set-0-start_time");

        if (talk_start_time) {
            talk_start_time.value = start;
            talk_start_time.readOnly = true;
            talk_start_time.classList.add("active-readonly");
            talk_start_time.dispatchEvent(new Event("input"));
        }
        if (talk_name_speaker) {
            talk_name_speaker.value = speaker;
            talk_name_speaker.readOnly = true;
            talk_name_speaker.classList.add("active-readonly");
            talk_name_speaker.dispatchEvent(new Event("input"));
        }
    } catch (error) {
        console.error("Erro ao carregar a palestra.", error);
    }
}

function cleanFields() {
    const talk_name_speaker = document.getElementById("id_itenstalk_set-0-name_speaker");
    const talk_start_time = document.getElementById("id_itenstalk_set-0-start_time");

    if (talk_name_speaker) {
        talk_name_speaker.value = "";
        talk_name_speaker.readOnly = false;
        talk_name_speaker.classList.remove("active-readonly");
        talk_name_speaker.dispatchEvent(new Event("input"));
    }

    if (talk_start_time) {
        talk_start_time.value = "";
        talk_start_time.readOnly = false;
        talk_start_time.classList.remove("active-readonly");
        talk_start_time.dispatchEvent(new Event("input"));
    }
}
