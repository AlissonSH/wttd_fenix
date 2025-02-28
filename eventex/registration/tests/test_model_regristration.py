from django.test import TestCase

from eventex.core.models import Talk, Course
from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


class RegistrationModelTestCase(TestCase):
    def setUp(self):
        self.students = Subscription.objects.create(
            name="Alisson Sielo Holkem",
            cpf="12345678901"
        )

        self.registration = Registration.objects.create(
            student=self.students,
            cpf=self.students.cpf,
            phone="55-99206-7827",
            observation="Aqui posso escrever algo."
        )

    def test_create(self):
        self.assertTrue(Registration.objects.exists())

    def test_has_registration(self):
        self.assertEqual(self.registration.student, self.students)
        self.assertEqual(self.registration.cpf, self.students.cpf)
        self.assertEqual(self.registration.phone, "55-99206-7827")
        self.assertEqual(self.registration.observation, "Aqui posso escrever algo.")

    def test_str(self):
        self.assertEqual("Alisson Sielo Holkem", str(self.registration))
