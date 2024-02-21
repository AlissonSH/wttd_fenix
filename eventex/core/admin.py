from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk
from django.utils.html import format_html


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "photo_link", "website_link", "phone", "email"]

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = "website"

    def photo_link(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_link.short_description = "foto"

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = "telefone"

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = "e-mail"


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
