from django.apps import AppConfig


class ForumConfig(AppConfig):
    """
    This app manages the forum functionality of the website,
    including posts, comments, and user interactions within
    the forum section.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
