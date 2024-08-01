from django.shortcuts import render


def matricula_list(request):
    template_name = "registration/matricula_list.html"
    return render(request, template_name)


def matricula_create(request):
    template_name = "registration/matricula_create.html"
    return render(request, template_name)
