from django.urls import path
from eventex.core.views import matricula_list

app_name = 'core'

urlpatterns = [
    path('listar/', matricula_list, name='matricula_list'),
]
