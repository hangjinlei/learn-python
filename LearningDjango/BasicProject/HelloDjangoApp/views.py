from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import os

# Create your views here.


def index(request):
    now = datetime.now()

    html_content = "<html><head><title>Hello, Django</title></head><body>"
    html_content += "<strong>Hello Django!</strong> on " + now.strftime(
        "%A, %d %B, %Y at %X"
    )
    html_content += "</body></html>"

    response_content = {"message": "Hello"}

    # return HttpResponse(html_content)
    # return JsonResponse(response_content)
    # return HttpResponse("Hello, Django!")
    return render(
        request=request,
        template_name="HelloDjangoApp/index.html",
    )


def about(request):
    return render(
        request=request,
        template_name="HelloDjangoApp/about.html",
        context={
            "title": "About HelloDjangoApp",
            "content": "Example app page for Django.",
        },
    )