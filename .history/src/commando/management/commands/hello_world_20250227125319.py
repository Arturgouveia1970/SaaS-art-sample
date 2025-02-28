from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any): # type: ignore
        print("Hello World")