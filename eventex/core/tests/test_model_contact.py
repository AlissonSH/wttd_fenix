from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            photo="https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg"
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value="alissonsieloholkem@gmail.com")

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value="55-99206-7827")

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind="A", value="B")
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value="alissonsieloholkem@gmail.com")
        self.assertEqual("alissonsieloholkem@gmail.com", str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            photo="https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg"
        )
        s.contact_set.create(kind=Contact.EMAIL, value="henrique@bastos.net")
        s.contact_set.create(kind=Contact.PHONE, value="21-996186180")

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ["henrique@bastos.net"]
        self.assertQuerySetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ["21-996186180"]
        self.assertQuerySetEqual(qs, expected, lambda o: o.value)
