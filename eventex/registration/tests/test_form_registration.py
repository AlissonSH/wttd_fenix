from django.template.defaultfilters import length
from django.test import TestCase

from eventex.core.models import Talk, Course
from eventex.registration.forms import RegistrationForm
from eventex.subscriptions.models import Subscription


class RegistrationFormTests(TestCase):
    def setUp(self):
        self.subscription = Subscription.objects.create(
            name="Alisson Sielo Holkem",
            cpf="12345678901",
            email="alissonsieloholkem@gmail.com",
            phone="55-99206-7827"
        )
        self.talks = Talk.objects.create(title="Python Brasil")
        self.course = Course.objects.create(title="Welcome To The Django", slots=20)

    def test_form_has_fields(self):
        form = RegistrationForm()
        self.assertSequenceEqual(
            ["student", "cpf", "phone", "talk", "name_speaker", "start_time", "observation"], list(form.fields))

    def test_form_cpf_digits(self):
        form = self.test_make_validated_form(cpf='ABcd5678901')
        self.assertFormErrorsCode(form, 'cpf', 'digits')

    def test_form_cpf_length(self):
        form = self.test_make_validated_form(cpf='12345')
        self.assertFormErrorsCode(form, 'cpf', 'length')

    def test_phone_is_optional(self):
        form = self.test_make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_observation_is_optional(self):
        form = self.test_make_validated_form(observation='')
        self.assertFalse(form.errors)

    def test_talk_is_optional(self):
        form = self.test_make_validated_form(talk='')
        self.assertFalse(form.errors)

    def test_name_speaker_is_optional(self):
        form = self.test_make_validated_form(name_speaker='')
        self.assertFalse(form.errors)

    def test_start_time_is_optional(self):
        form = self.test_make_validated_form(start_time='')
        self.assertFalse(form.errors)

    def test_make_validated_form(self, **kwargs):
        values = dict(
            student=self.subscription.id,
            cpf=self.subscription.cpf,
            phone="55-99206-7827",
            talk=self.talks.id,
            name_speaker="Henrique Bastos",
            start_time="08:30",
            observation="Aqui posso escrever algo."
        )

        data = dict(values, **kwargs)
        form = RegistrationForm(data)
        form.is_valid()
        return form

    def assertFormErrorsCode(self, form, fields, code):
        error = form.errors.as_data()
        error_list = error[fields][0]
        self.assertEquals(code, error_list.code)

    def test_talk_without_course(self):
        talks2 = Talk.objects.create(title='Django Brasil')

        form = RegistrationForm()

        self.assertIn(self.talks, form.fields['talk'].queryset)
        self.assertIn(talks2, form.fields['talk'].queryset)
        self.assertNotIn(self.course, form.fields['talk'].queryset)
