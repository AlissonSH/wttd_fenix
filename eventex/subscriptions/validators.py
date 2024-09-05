from django.core.exceptions import ValidationError


def validate_cpf(value):
    cleaned_value = value.replace('.', '').replace('-', '')
    if not cleaned_value.isdigit():
        raise ValidationError('CPF deve contar apenas números!', 'digits')
    if len(cleaned_value) != 11:
        raise ValidationError('CPF deve conter 11 números!', 'length')
