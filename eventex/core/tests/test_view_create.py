from django.test import TestCase
from django.shortcuts import resolve_url as r


class RegisterListView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:create_list'))

    def test_get(self):
        """Get /create/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/create_list.html')
