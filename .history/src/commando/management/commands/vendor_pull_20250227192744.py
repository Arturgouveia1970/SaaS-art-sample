from django.core.management.base import BaseCommand
from typing import Any

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World")