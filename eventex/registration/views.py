import pprint
from audioop import reverse
from pyexpat.errors import messages

from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.reverse import reverse_lazy
from django.contrib import messages
from eventex.registration.forms import RegistrationForm, TalkFormSet, CourseFormSet
from eventex.registration.models import Registration
from django.views.generic import ListView, CreateView



class MatriculaListView(ListView):
    model = Registration
    template_name = "registration/matricula_list.html"


class MatriculaCreateView(CreateView):
    model = Registration
    template_name = "registration/matricula_create.html"
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talk_formset'] = TalkFormSet(self.request.POST or None, instance=self.object)
        context['course_formset'] = CourseFormSet(self.request.POST or None, instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        talk_formset = context['talk_formset']
        course_formset = context['course_formset']

        try:
            with transaction.atomic():
                self.object = form.save(commit=False)
                self.object.save()

                if (
                        (talk_formset.is_valid() and any(f.cleaned_data for f in talk_formset)) or
                        (course_formset.is_valid() and any(f.cleaned_data for f in course_formset))
                ):
                    _save_talk(talk_formset, self.object)
                    _save_course(course_formset, self.object)

                    return redirect(self.get_success_url())
                else:
                    messages.error(self.request, "Selecione pelo menos uma palestra ou curso.")
                    return super().form_invalid(form)
        except Exception as e:
            messages.error(self.request, str(e))
            return super().form_invalid(form)


    def get_success_url(self):
        messages.success(self.request, 'Matrícula registrada com sucesso!')
        return reverse_lazy('registration:matricula_list')

def _save_talk(talk_formset, obj):
    if talk_formset.is_valid():
        talk_formset.instance = obj
        talk_formset.save()
    else:
        raise Exception("Dados das Palestras Inválidos.")

def _save_course(course_formset, obj):
    if course_formset.is_valid():
        course_formset.instance = obj
        course_formset.save()
    else:
        raise Exception("Dados dos Cursos Inválidos.")
