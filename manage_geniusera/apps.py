from django.apps import AppConfig


class ManagegeniuseraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_geniusera'

    def ready(self) -> None:
         import manage_geniusera.signals
