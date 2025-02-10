from django.template.defaultfilters import length
from django.test import TestCase

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

    def test_form_has_fields(self):
        form = RegistrationForm()
        self.assertSequenceEqual(
            ["student", "cpf", "phone", "observation"], list(form.fields))

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

    def test_make_validated_form(self, **kwargs):
        values = dict(
            student=self.subscription.id,
            cpf=self.subscription.cpf,
            phone="55-99206-7827",
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
