from django.urls import path
from eventex.core.views import matricula_list, matricula_create

app_name = 'core'

urlpatterns = [
    path('listar/', matricula_list, name='matricula_list'),
    path('create/', matricula_create, name='matricula_create'),
]
