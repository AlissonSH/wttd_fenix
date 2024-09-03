$(document).ready(function () {
    aplicarMascaras();
});

function aplicarMascaras() {
    $('.mask_cpf').mask('999.999.999-99', {reverse: true});
    $('.mask_phone').mask('99-99999-9999', {reverse: true, autoclear: false});
}
