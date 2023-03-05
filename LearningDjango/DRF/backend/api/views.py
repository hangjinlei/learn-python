from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import json

# Create your views here.


def api_home(request: HttpRequest, *args, **kwargs):
    body = request.body  # bytes string --> json
    data = {}
    try:
        data = json.loads(body)
        data["headers"] = dict(request.headers)
        data["content_type"] = request.content_type
        data["params"] = dict(request.GET)
    except:
        pass

    # print(data)
    return JsonResponse(data)
