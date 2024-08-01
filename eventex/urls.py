from django.contrib import admin
from django.urls import path, include
from eventex.core.views import home, speaker_detail, talk_list

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    path('matricula/', include('eventex.registration.urls')),
    path('', include('eventex.core.urls')),
    path('admin/', admin.site.urls),
]
