from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args: any, **options: any): # type: ignore
        print("Hello World")