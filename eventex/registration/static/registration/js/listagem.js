$(document).ready(function () {
    getTabelaStudents();
});

const getTabelaStudents = () => {
    axios.get(URL_STUDENT_LIST)
        .then(response => {
            $("#idTabela > tbody").empty();

            if (response['data'].length === 0) {
                $("#idTabela").find('tbody').append(`
                    <tr>
                        <td colspan="6" class="text-center text-danger">Nenhum dado encontrado.</td>                        
                    </tr>
                `);
            } else {
                response['data'].forEach(estudante => {
                    $("#idTabela").find('tbody').append(`
                        <tr>
                            <td class="text-center"><input type="checkbox" class="student-checkbox"></td>
                            <td class="text-center">${estudante.student}</td>
                            <td class="text-center">${estudante.student_name}</td>
                            <td class="text-center">${estudante.cpf}</td>
                            <td class="text-center">${estudante.phone}</td>
                            <td class="text-center">${estudante.student_paid ? '<i class="text-success bi bi-check-circle"></i>' : '<i class="text-danger bi bi-x-circle"></i>'}</td>                        
                        </tr>
                    `);
                });
            }
        })
        .catch(error => {
            console.error('Erro ao buscar os dados dos estudantes:', error);
        });
}
