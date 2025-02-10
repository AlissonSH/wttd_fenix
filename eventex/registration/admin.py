from django.contrib import admin

from eventex.registration.forms import ItensTalkForm, ItensCourseForm, RegistrationForm
from eventex.registration.models import Registration, ItensTalk, ItensCourse


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('student', 'cpf', 'phone')


class ItensTalkAdmin(admin.ModelAdmin):
    form = ItensTalkForm
    list_display = ("talk", "get_registration", "name_speaker", "start_time")

    def get_registration(self, obj):
        return obj.registration
    get_registration.short_description = "Estudante"



class ItensCourseAdmin(admin.ModelAdmin):
    form = ItensCourseForm
    list_display = ("course", "get_registration", "name_speaker", "start_time")

    def get_registration(self, obj):
        return obj.registration

    get_registration.short_description = "Estudante"


admin.site.register(Registration, RegistrationModelAdmin)
admin.site.register(ItensTalk, ItensTalkAdmin)
admin.site.register(ItensCourse, ItensCourseAdmin)
