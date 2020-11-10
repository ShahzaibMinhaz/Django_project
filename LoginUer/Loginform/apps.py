from django.apps import AppConfig


class LoginformConfig(AppConfig):
    name = 'Loginform'

    def ready(self):
        import Loginform.signals