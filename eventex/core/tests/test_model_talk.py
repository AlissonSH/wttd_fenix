from django.test import TestCase
from eventex.core.managers import PeriodManager
from eventex.core.models import Talk, Course


class TalkModelsTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title="Título da Palestra",
        )
        self.talk2 = Talk.objects.create(
            title="Título da Palestra 2",
        )
        self.course = Course.objects.create(
            title="Título do Curso",
            slots=20
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            website="http://henriquebastos.net",
        )

        self.assertEqual(1, self.talk.speakers.count())

    def test_start_blank(self):
        field = Talk._meta.get_field("start")
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field("start")
        self.assertTrue(field.null)

    def test_description_blank(self):
        field = Talk._meta.get_field("description")
        self.assertTrue(field.blank)

    def test_speakers_blank(self):
        field = Talk._meta.get_field("speakers")
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual("Título da Palestra", str(self.talk))

    def test_ordering(self):
        self.assertListEqual(["start"], Talk._meta.ordering)

    def test_just_talk(self):
        talks = Talk.just_talk()
        self.assertIn(self.talk, talks)
        self.assertIn(self.talk2, talks)
        self.assertNotIn(self.course, talks)

    def test_just_talk_when_all_if_no_course(self):
        Course.objects.all().delete()
        talks = Talk.just_talk()
        self.assertIn(self.talk, talks)
        self.assertIn(self.talk2, talks)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title="Morning_talk", start="11:59")
        Talk.objects.create(title="Afternoon_talk", start="12:00")

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ["Morning_talk"]
        self.assertQuerySetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ["Afternoon_talk"]
        self.assertQuerySetEqual(qs, expected, lambda o: o.title)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Título do Curso",
            start="09:00",
            description="Descrição do curso.",
            slots=20
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speaker(self):
        self.course.speakers.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            website="http://henriquebastos.net",
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual("Título do Curso", str(self.course))

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)

    def test_ordering(self):
        self.assertListEqual(["start"], Course._meta.ordering)
