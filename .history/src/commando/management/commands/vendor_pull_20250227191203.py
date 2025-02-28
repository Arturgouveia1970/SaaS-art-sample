from django.core.management.base import BaseCommand
from typing import Any

vendor_

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World")