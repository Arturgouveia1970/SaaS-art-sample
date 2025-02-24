import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    print()
    html_ = ""
    return HttpResponse("<h1>Hello world</h1>")