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
