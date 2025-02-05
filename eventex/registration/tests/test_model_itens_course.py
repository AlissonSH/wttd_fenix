from django.test import TestCase

from eventex.core.models import Course
from eventex.registration.models import Registration, ItensCourse
from eventex.subscriptions.models import Subscription


class ModelItensCourseTest(TestCase):
    def setUp(self):
        self.registration = Registration.objects.create(
            student=Subscription.objects.create(name="Alisson Sielo Holkem"))

        self.course = Course.objects.create(title="Titulo do Curso", slots=20)

        self.item_course = ItensCourse.objects.create(
            registration=self.registration,
            course=self.course,
            name_speaker="Henrique Bastos",
            start_time="14:00"
        )

    def test_create(self):
        self.assertTrue(ItensCourse.objects.exists())
        self.assertEqual(ItensCourse.objects.count(), 1)

    def test_str(self):
        self.assertEqual(str(self.item_course), "Titulo do Curso")

    def test_field_null_blank(self):
        fields = {
            "registration": (False, False),
            "name_speaker": (True, True),
            "start_time": (True, True),
            "course": (True, True),
        }

        for field_name, (null_value, blank_value) in fields.items():
            with self.subTest(valor=field_name):
                field = ItensCourse._meta.get_field(field_name)
                self.assertEqual(field.null, null_value)
                self.assertEqual(field.blank, blank_value)
