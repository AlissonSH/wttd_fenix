from django.urls import path
from eventex.registration.views import matricula_list, matricula_create

app_name = 'registration'

urlpatterns = [
    path('listar/', matricula_list, name='matricula_list'),
    path('create/', matricula_create, name='matricula_create'),
]
