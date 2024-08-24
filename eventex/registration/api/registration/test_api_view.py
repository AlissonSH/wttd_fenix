from rest_framework.test import APITestCase
from django.urls import reverse as r


class RegistrationViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = r('registration:student-select2')
        self.resp = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_request_get_without_term(self):
        self.assertEqual(200, self.resp.status_code)
        self.assertEqual(self.resp.json(), {"results": []})

    def test_request_get_with_term(self):
        query = self.client.get(self.url, {'term': ''})
        self.assertEqual(200, query.status_code)
        self.assertEqual(query.json(), {"results": []})
