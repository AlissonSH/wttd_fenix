from django import forms
from eventex.registration.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student', 'cpf', 'phone', 'observation']
