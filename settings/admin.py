from django.contrib import admin
from .models import Settings



@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_background_color', 'site_text_color')
    def has_add_permission(self, request):
        # Zaten kayıt varsa yeni eklemeyi engelle
        return not Settings.objects.exists()

short_description = 'Site Ayarları'
