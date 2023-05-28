from django.apps import AppConfig


class CollegeConfig(AppConfig):
    name = 'college'
    def ready(self):
        import college.mysignal