from rest_framework import status
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase
from django.urls import reverse as r

from eventex.core.models import Talk, Speaker
from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


class RegistrationViewSetSelect2Test(APITestCase):
    def setUp(self):
        self.url = r('registration:registration-select2')
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


class RegistrationViewSetGetDadosStudentTest(APITestCase):
    def setUp(self):
        self.url = r('registration:registration-get-dados-student')
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
        self.student.cpf = '12345678910'
        self.student.phone = ''
        self.student.save()

        response = self.client.get(self.url, {'id': self.student.id})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {'cpf': self.student.cpf, 'phone': None})

    def test_get_dados_student_cpf_and_phone_valid(self):
        self.student.cpf = '12345678910'
        self.student.phone = '55-99206-7827'
        self.student.save()

        response = self.client.get(self.url, {'id': self.student.id})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {'cpf': self.student.cpf, 'phone': self.student.phone})


class RegistrationViewSetListTest(APITestCase):
    def setUp(self):
        self.student = Subscription.objects.create(name='Alisson Sielo Holkem', paid=True)
        self.registration = Registration.objects.create(
            student=self.student, cpf='123.456.789-10', phone='55-99206-7827')

        self.url = r('registration:registration-list')
        self.resp = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_student_list(self):
        self.assertEqual(200, self.resp.status_code)
        data = self.resp.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['student'], self.student.id)
        self.assertEqual(data[0]['student_name'], self.student.name)
        self.assertEqual(data[0]['cpf'], self.registration.cpf)
        self.assertEqual(data[0]['phone'], self.registration.phone)
        self.assertEqual(data[0]['student_paid'], self.student.paid)

    def test_student_list_phone_empty(self):
        self.registration.phone = ''
        self.registration.save()

        self.resp = self.client.get(self.url)
        self.assertEqual(self.resp.status_code, HTTP_200_OK)
        data = self.resp.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['phone'], '')


class RegistrationViewSetGetDadosTalkTest(APITestCase):
    def setUp(self):
        self.url = r('registration:registration-get-dados-talk')
        self.resp = self.client.get(self.url)
        self.talk = Talk.objects.create(title='Python Brasil', start="08:30")
        self.speaker = Speaker.objects.create(name='Henrique Bastos')
        self.talk.speakers.add(self.speaker)

    def test_get(self):
        response = self.client.get(self.url, {'id': self.talk.id})
        self.assertEqual(200, response.status_code)

    def test_get_dados_talk(self):
        response = self.client.get(self.url, {'id': self.talk.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['start'], "08:30")
        self.assertEqual(response.data['speaker'][0], self.speaker.name)

    def test_talk_with_multiple_speakers(self):
        speaker2 = Speaker.objects.create(name='Grace Hopper')
        self.talk.speakers.add(speaker2)
        response = self.client.get(self.url, {'id': self.talk.id})
        self.assertEqual(200, response.status_code)

        speaker_all = [speaker.name for speaker in self.talk.speakers.all()]
        self.assertEqual(response.data['speaker'], speaker_all)
