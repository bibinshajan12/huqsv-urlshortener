from django.contrib import admin
from .models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'original_url', 'created_at', 'created_by')  # Ensure fields are correctly referenced

admin.site.register(ShortURL, ShortURLAdmin)
