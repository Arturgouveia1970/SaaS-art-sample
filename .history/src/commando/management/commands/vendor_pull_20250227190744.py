from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Anyny): # type: ignore
        print("Hello World")