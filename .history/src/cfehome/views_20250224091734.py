import pathlib
from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_co
    html_ = ""
    html_file_path = this_dir / "home.html"
    return HttpResponse("<h1>Hello world</h1>")