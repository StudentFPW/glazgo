from django.apps import AppConfig


class AtsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ats"

    def ready(self):
        from . import signals