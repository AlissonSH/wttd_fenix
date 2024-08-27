from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventex.registration.api.registration.views import StudentViewSet

from eventex.registration.models import Registration
from eventex.registration.views import matricula_list, matricula_create

app_name = 'registration'
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),

    path('listar/', matricula_list, name='matricula_list'),
    path('create/', matricula_create, name='matricula_create'),
]
