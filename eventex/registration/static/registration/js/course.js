document.addEventListener('DOMContentLoaded', () => {
    const itensCourse = document.querySelector("#id_itenscourse_set-0-course");

    $(itensCourse).on('change', async function () {
        await getDadosCourse();
    });
});

async function getDadosCourse() {
    const idCourse = document.querySelector("#id_itenscourse_set-0-course")?.value;

    if (!idCourse) {
        cleanFields();
        return
    }
    try {
        const response = await axios.get(URL_DADOS_COURSE_AXIOS, {
            params: {
                id: idCourse,
            }
        });

        const {start, speaker} = response.data
        const course_name_speaker = document.getElementById("id_itenscourse_set-0-name_speaker");
        const course_start_time = document.getElementById("id_itenscourse_set-0-start_time");

        if (course_start_time) {
            course_start_time.value = start;
            course_start_time.readOnly = true;
            course_start_time.classList.add("active-readonly");
            course_start_time.dispatchEvent(new Event("input"));
        }
        if (course_name_speaker) {
            course_name_speaker.value = speaker;
            course_name_speaker.readOnly = true;
            course_name_speaker.classList.add("active-readonly");
            course_name_speaker.dispatchEvent(new Event("input"));
        }
    } catch (error) {
        console.error("Erro ao carregar o curso.", error);
    }
}

function cleanFields() {
    const course_name_speaker = document.getElementById("id_itenscourse_set-0-name_speaker");
    const course_start_time = document.getElementById("id_itenscourse_set-0-start_time");

    if (course_name_speaker) {
        course_name_speaker.value = "";
        course_name_speaker.readOnly = false;
        course_name_speaker.classList.remove("active-readonly");
        course_name_speaker.dispatchEvent(new Event("input"));
    }

    if (course_start_time) {
        course_start_time.value = "";
        course_start_time.readOnly = false;
        course_start_time.classList.remove("active-readonly");
        course_start_time.dispatchEvent(new Event("input"));
    }
}
