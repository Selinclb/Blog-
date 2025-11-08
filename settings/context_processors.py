from .models import Settings

def site_settings(request):
    try:
        return {'site_config': Settings.objects.first()}
    except Exception:
        return {'site_config': None}