from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.registration.forms import RegistrationForm


class MatriculaListView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('registration:matricula_list'))

    def test_get(self):
        """Get /create/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'registration/matricula_list.html')

    def test_creates_link(self):
        expected = 'href="{}"'.format(r('registration:matricula_create'))
        self.assertContains(self.resp, expected)


class MatriculaCreateView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('registration:matricula_create'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'registration/matricula_create.html')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RegistrationForm)

    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertSequenceEqual(['student', 'cpf', 'phone', 'observation'], list(form.fields))
