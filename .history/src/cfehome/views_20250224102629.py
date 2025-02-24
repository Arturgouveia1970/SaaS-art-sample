import pathlib
from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "My Page Porra"
    my_context = {
        "page_title": my_title
    }
    html_template = "home.html"
    
    return render(request, html_template, my_context)


def my_old_homt_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!DOCTYPE html>
<html>

<body>
    <h1>{page_title} anything?</h1>
</body>
</html>    
""".format(**my_context) # page_title=my_title
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)

VALID_CODE = "abc123"