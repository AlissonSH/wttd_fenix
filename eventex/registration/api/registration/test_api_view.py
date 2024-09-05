from rest_framework import status
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase
from django.urls import reverse as r
from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


class RegistrationViewSetSelect2TestCase(APITestCase):
    def setUp(self):
        self.url = r('registration:student-select2')
        self.resp = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_request_get_without_term(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(self.resp.json(), {"results": []})

    def test_request_get_with_term_empty(self):
        query = self.client.get(self.url, {'term': ''})
        self.assertEqual(200, query.status_code)
        self.assertEqual(query.json(), {"results": []})

    def test_request_get_with_invalid_term(self):
        student_name = 'Alisson Sielo Holkem'
        student= Subscription.objects.create(name=student_name)
        Registration.objects.create(student=student)

        query = self.client.get(self.url, {'term': 'Pedro'})
        self.assertEqual(200, query.status_code)
        self.assertEqual(query.json(), {"results": []})

    def test_request_get_with_valid_term(self):
        student_name = 'Alisson Sielo Holkem'
        student = Subscription.objects.create(name=student_name)
        Registration.objects.create(student=student)

        query = self.client.get(self.url, {'term': 'Alisson Sielo Holkem'})
        self.assertEqual(200, query.status_code)

        results = query.json().get('results', [])
        self.assertGreater(len(results), 0)
        self.assertIn(student_name, [results['text'] for results in results])


class RegistrationViewSetGetDadosStudentTestCase(APITestCase):
    def setUp(self):
        self.url = r('registration:student-get-dados-student')
        self.resp = self.client.get(self.url)
        self.student = Subscription.objects.create(name='Alisson Sielo Holkem')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_get_dados_student_cpf_empty(self):
        self.student.cpf = ''
        self.student.save()

        response = self.client.get(self.url, {'id': self.student.id})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'cpf': None})

    def test_get_dados_student_cpf_and_phone_empty(self):
        self.student.cpf = '123.456.789-10'
        self.student.phone = ''
        self.student.save()

        response = self.client.get(self.url, {'id': self.student.id})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {'cpf': self.student.cpf, 'phone': None})

    def test_get_dados_student_cpf_and_phone_valid(self):
        self.student.cpf = '123.456.789-10'
        self.student.phone = '55-99206-7827'
        self.student.save()

        response = self.client.get(self.url, {'id': self.student.id})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {'cpf': self.student.cpf, 'phone': self.student.phone})
