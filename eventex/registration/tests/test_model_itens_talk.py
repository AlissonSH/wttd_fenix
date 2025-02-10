from django.test import TestCase

from eventex.core.models import Talk
from eventex.registration.models import Registration, ItensTalk
from eventex.subscriptions.models import Subscription


class ModelItensTalkTest(TestCase):
    def setUp(self):
        self.registration = Registration.objects.create(
            student=Subscription.objects.create(name="Alisson Sielo Holkem"))

        self.talk = Talk.objects.create(title="Titulo da Palestra")

        self.item_talk = ItensTalk.objects.create(
            registration=self.registration,
            talk=self.talk,
            name_speaker="Henrique Bastos",
            start_time="10:00",
        )

    def test_create(self):
        self.assertTrue(ItensTalk.objects.exists())
        self.assertEqual(ItensTalk.objects.count(), 1)

    def test_str(self):
        self.assertEqual(str(self.item_talk), "Titulo da Palestra")

    def test_field_null_blank(self):
        fields = {
            "registration": (False, False),
            "name_speaker": (True, True),
            "start_time": (True, True),
            "talk": (True, True),
        }

        for field_name, (null_value, blank_value) in fields.items():
            with self.subTest(valor=field_name):
                field = ItensTalk._meta.get_field(field_name)
                self.assertEqual(field.null, null_value)
                self.assertEqual(field.blank, blank_value)
