from django.apps import AppConfig


class ProfilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiler'

    # add profiler automatically on user registration
    def ready(self):
        import profiler.signals
