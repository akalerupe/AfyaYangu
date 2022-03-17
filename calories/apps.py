from django.apps import AppConfig


class CaloriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calories'

    def ready(self): 
        """intiate signals for them to work"""
        import calories.signals 
