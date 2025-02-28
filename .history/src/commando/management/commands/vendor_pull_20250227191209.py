from django.core.management.base import BaseCommand
from typing import Any

vendor_staticfiles

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World")