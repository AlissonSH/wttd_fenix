from django.shortcuts import render, redirect
from eventex.registration.forms import RegistrationForm


def matricula_list(request):
    template_name = "registration/matricula_list.html"
    return render(request, template_name)


def matricula_create(request):
    template_name = "registration/matricula_create.html"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration:matricula_list")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, template_name, context)
