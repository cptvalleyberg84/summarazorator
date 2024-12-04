from django.apps import AppConfig


class ProfilerConfig(AppConfig):
    """
    This app handles user profiles and their related functionality.
    It automatically creates user profiles upon user registration
    using Django signals.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiler'

    # add profiler automatically on user registration
    def ready(self):
        import profiler.signals
