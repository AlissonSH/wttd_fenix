from django.urls import path
from eventex.core.views import create_list

app_name = 'core'

urlpatterns = [
    path('', create_list, name='create_list'),
]
