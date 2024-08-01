from django.urls import path
from eventex.core.views import talk_list, speaker_detail

app_name = 'core'

urlpatterns = [
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
]
