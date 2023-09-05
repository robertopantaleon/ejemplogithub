from django.apps import AppConfig


# Como se llama nuestra app
class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
