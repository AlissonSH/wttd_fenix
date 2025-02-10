from django.test import TestCase

from eventex.core.models import Talk, Course
from eventex.registration.forms import ItensTalkForm, TalkFormSet


class ItensTalkFormTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title="Titulo da Palestra")
        self.talk2 = Talk.objects.create(title="Titulo da Palestra 2")
        self.course = Course.objects.create(title="Titulo do Curso", slots=20)

    def test_form_fields_itens_talk(self):
        form = ItensTalkForm()
        self.assertEqual(["talk"], list(form.fields.keys()))

    def test_form_fields_talk_formset(self):
        formset = TalkFormSet()
        form = formset.forms[0]

        expected = {"talk", "name_speaker", "start_time"}
        self.assertTrue(expected.issubset(list(form.fields.keys())))

    def test_form_is_valid(self):
        form = self.test_make_validated_form()
        self.assertTrue(form.is_valid())

    def test_invalid_talk(self):
        form = self.test_make_validated_form(talk=9999)
        self.assertFalse(form.is_valid())
        self.assertIn("talk", form.errors)

    def test_talk_is_optional(self):
        form = self.test_make_validated_form(talk=None)
        self.assertTrue(form.is_valid())

    def test_name_speaker_is_optional(self):
        form = self.test_make_validated_form(name_speaker="")
        self.assertFalse(form.errors)

    def test_start_time_is_optional(self):
        form = self.test_make_validated_form(start_time="")
        self.assertFalse(form.errors)

    def test_make_validated_form(self, **kwargs):
        values = dict(
            talk=self.talk.id,
            name_speaker="Henrique Bastos",
            start_time="10:00",
        )
        data = dict(values, **kwargs)
        form = ItensTalkForm(data)

        form.is_valid()
        return form

    def test_just_talk(self):
        talks = Talk.just_talk()
        self.assertIn(self.talk, talks)
        self.assertIn(self.talk2, talks)
        self.assertNotIn(self.course, talks)

    def test_talk_queryset(self):
        form = ItensTalkForm()
        self.assertEqual(list(form.fields["talk"].queryset), list(Talk.just_talk()))
