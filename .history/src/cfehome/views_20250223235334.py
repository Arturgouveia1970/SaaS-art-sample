import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file)

def home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")