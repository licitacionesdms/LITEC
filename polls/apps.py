from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    # verbose_name = 'perfiles'

    # def ready(self):
    #     import polls.signals

