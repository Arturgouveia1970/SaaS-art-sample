from django.core.management.base import BaseCommand
from typing import Any

VENDOR_STATICFILES = {
    f"lowbite.min.css"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World")