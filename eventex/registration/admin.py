from django.contrib import admin
from eventex.registration.models import Registration


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('student', 'cpf', 'phone')

admin.site.register(Registration, RegistrationModelAdmin)
