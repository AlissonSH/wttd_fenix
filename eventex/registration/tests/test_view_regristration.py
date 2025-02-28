from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Talk, Course
from eventex.registration.forms import RegistrationForm
from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


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
        self.assertSequenceEqual(
            ['student', 'cpf', 'phone', 'observation'], list(form.fields))


class RegistrationPostValid(TestCase):
    def setUp(self):
        self.student = Subscription.objects.create(
            name="Alisson Sielo Holkem",
            cpf="12345678901",
        )
        self.talks = Talk.objects.create(title="Python Brasil")
        self.course = Course.objects.create(title="Welcome To The Django", slots=20)

        self.context = {
            "student": self.student.id,
            "cpf": self.student.cpf,
            "phone": "55-99206-7827",
            "observation": "Aqui posso escrever algo.",

            "itenstalk_set-TOTAL_FORMS": "1",
            "itenstalk_set-INITIAL_FORMS": "0",
            "itenstalk_set-0-talk": str(self.talks.id),

            "itenscourse_set-TOTAL_FORMS": "1",
            "itenscourse_set-INITIAL_FORMS": "0",
            "itenscourse_set-0-course": str(self.course.id),
        }

        self.resp = self.client.post(r('registration:matricula_create'), self.context)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_redirect_after_post_valid(self):
        self.assertRedirects(self.resp, r('registration:matricula_list'))

    def test_save_registration(self):
        self.assertTrue(Registration.objects.exists())
