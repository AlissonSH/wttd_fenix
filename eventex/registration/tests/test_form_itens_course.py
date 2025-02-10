from django.test import TestCase

from eventex.core.models import Course
from eventex.registration.forms import ItensCourseForm, CourseFormSet


class FormItensCourseTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title="Titulo do Curso", slots=20)

    def test_field_itens_course(self):
        form = ItensCourseForm()
        self.assertEqual(["course", "name_speaker", "start_time"], list(form.fields.keys()))

    def test_field_course_formset(self):
        formset = CourseFormSet()
        form = formset.forms[0]

        expected = {'course', 'name_speaker', 'start_time'}
        self.assertTrue(expected.issubset(list(form.fields.keys())))

    def test_make_validated_form(self, **kwargs):
        values = dict(
            course=self.course.id,
            name_speaker="Henrique Bastos",
            start_time="14:00",
        )
        data = dict(values, **kwargs)
        form = ItensCourseForm(data)

        form.is_valid()
        return form

    def test_form_is_valid(self):
        form = self.test_make_validated_form()
        self.assertTrue(form.is_valid())

    def test_course_is_invalid(self):
        form = self.test_make_validated_form(course=99999)
        self.assertFalse(form.is_valid())
        self.assertIn("course", form.errors)

    def test_course_is_optional(self):
        form = self.test_make_validated_form(course=None)
        self.assertTrue(form.is_valid())

    def test_name_speaker_is_optional(self):
        form = self.test_make_validated_form(name_speaker="")
        self.assertTrue(form.is_valid())

    def test_start_time_is_optional(self):
        form = self.test_make_validated_form(start_time="")
        self.assertTrue(form.is_valid())
