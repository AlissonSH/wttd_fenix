from django.shortcuts import render
from eventex.registration.forms import RegistrationForm


def matricula_list(request):
    template_name = "registration/matricula_list.html"
    return render(request, template_name)


def matricula_create(request):
    template_name = "registration/matricula_create.html"
    context = {'form': RegistrationForm()}
    return render(request, template_name, context)
