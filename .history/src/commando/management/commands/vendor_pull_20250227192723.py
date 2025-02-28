from django.core.management.base import BaseCommand
from typing import Any

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World")