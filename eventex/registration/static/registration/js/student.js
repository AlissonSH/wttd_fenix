document.addEventListener('DOMContentLoaded', () => {
    const elementsSelect2 = document.querySelectorAll(".form_select2");

    elementsSelect2.forEach((elem) => {
        $(elem).select2({
            placeholder: "",
            allowClear: true,
            width: '100%'
        });
    });

    const elementStudent = document.querySelector("#id_student");
    $(elementStudent).select2({
        ajax: {
            delay: 500,
            url: URL_LISTA_STUDENT_AJAX,
            dataType: 'json'
        }
    });

    const cpfId = document.getElementById("id_cpf");
    const phoneId = document.getElementById("id_phone");
    if (!elementStudent.value) {
        cpfId.value = "";
        phoneId.value = "";
    }

    $(elementStudent).on('change', async function(){
        await getDadosStudent();
    });
});

async function getDadosStudent() {
    const studentId = document.querySelector("#id_student")?.value;
    try {
        const response = await axios.get(URL_DADOS_STUDENT_AXIOS, {
            params: {
                id: studentId,
            }
        });
        const {cpf, phone} = response.data
        const cpfValue = document.getElementById("id_cpf");
        const phoneValue = document.getElementById("id_phone");
        if (cpfValue) {
            cpfValue.value = cpf;
            cpfValue.classList.add("mask_cpf");
            cpfValue.dispatchEvent(new Event("input"));
        }
        if (phoneValue) {
            phoneValue.value = phone;
            phoneValue.classList.add("mask_phone");
            phoneValue.dispatchEvent(new Event("input"))
        }
    } catch (error) {
        console.error("Erro ao carregar o estudante.", error);
    }
}
