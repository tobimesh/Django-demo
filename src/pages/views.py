from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *arg, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *arg, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")
    return render(request, "contact.html", {})


def about_view(request, *arg, **kwargs):
    # return HttpResponse("<h1>About page</h1>")
    my_context = {
        "title": "This is about us",
        "my_number": 123,
        "my_list": [123, 353, 3535, "Abc"],
        "my_html": "<h1>Hello world</h1>",
    }
    return render(request, "about.html", my_context)


# def service_view(*arg, **kwargs):
#     return HttpResponse("<h1>Service page</h1>")


def service_view(request, *arg, **kwargs):
    return render(request, "service.html", {})
