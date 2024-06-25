from django.shortcuts import render
from django.views.generic import ListView, DetailView
from eventex.core.models import Speaker, Talk


home = ListView.as_view(template_name="index.html", model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)


def matricula_list(request):
    template_name = "core/matricula_list.html"
    return render(request, template_name)
