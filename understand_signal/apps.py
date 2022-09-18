from django.apps import AppConfig


class UnderstandSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'understand_signal'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import understand_signal.signals

