from django.apps import AppConfig


class VmsConfig(AppConfig):
    name = 'VMS'
    def ready(self):
        import VMS.signals
