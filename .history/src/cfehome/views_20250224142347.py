import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter()
    my_title = "My Page Porra"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count()
    }
    path = request.path
    print("path", path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_homt_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        
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