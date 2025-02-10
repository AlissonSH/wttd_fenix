from django import forms
from django.forms import inlineformset_factory

from eventex.core.models import Talk
from eventex.registration.models import Registration, ItensTalk, ItensCourse


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["student", "cpf", "phone", "observation"]


class ItensTalkForm(forms.ModelForm):
    class Meta:
        model = ItensTalk
        fields = ["talk"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["talk"].queryset = Talk.just_talk()


TalkFormSet = inlineformset_factory(
    Registration,
    ItensTalk,
    form=ItensTalkForm,
    fields=("talk", "name_speaker", "start_time"),
    extra=1,
)


class ItensCourseForm(forms.ModelForm):
    class Meta:
        model = ItensCourse
        fields = ["course", "name_speaker", "start_time"]


CourseFormSet = inlineformset_factory(
    Registration,
    ItensCourse,
    form=ItensCourseForm,
    fields=("course", "name_speaker", "start_time"),
    extra=1,
)
