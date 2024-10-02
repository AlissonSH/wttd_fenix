from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventex.registration.api.registration.views import StudentViewSet
from eventex.registration.views import MatriculaListView, MatriculaCreateView

app_name = 'registration'
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),

    path('listar/', MatriculaListView.as_view(), name='matricula_list'),
    path('create/', MatriculaCreateView.as_view(), name='matricula_create'),
]
