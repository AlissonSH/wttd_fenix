from django import forms

from eventex.core.models import Talk, Course
from eventex.registration.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["student", "cpf", "phone", "talk", "name_speaker", "start_time", "observation"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["talk"].queryset = Talk.objects.exclude(pk__in=Course.objects.values_list('pk', flat=True))
