from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Alisson Sielo Holkem', cpf='12345678901',
                    email='alissonsieloholkem@gmail.com', phone='55-99206-7827')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEquals(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEquals(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'alissonsieloholkem@gmail.com']

        self.assertEquals(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Alisson Sielo Holkem',
                    '12345678901',
                    'alissonsieloholkem@gmail.com',
                    '55-99206-7827']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
