from audioop import reverse
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from rest_framework.reverse import reverse_lazy
from django.contrib import messages
from eventex.registration.forms import RegistrationForm
from eventex.registration.models import Registration
from django.views.generic import ListView, CreateView



class MatriculaListView(ListView):
    model = Registration
    template_name = "registration/matricula_list.html"


class MatriculaCreateView(CreateView):
    model = Registration
    template_name = "registration/matricula_create.html"
    form_class = RegistrationForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Matrícula registrada com sucesso!')
        return reverse_lazy('registration:matricula_list')
