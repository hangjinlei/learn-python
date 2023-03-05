from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def sya_hello(request: HttpRequest, name: str):
    # return HttpResponse("Hello World")
    return render(request, "hello.html", {"name": name})
