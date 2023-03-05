from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.


rooms = [
    {"id": 1, "name": "Lets learn Python!"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontent developers"},
]


def home(request: HttpRequest):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(Q(topic__name__contains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q)
                                )
    rooms_count = rooms.count()

    topics = Topic.objects.all()

    context = {"rooms": rooms, "topics": topics, "rooms_count": rooms_count}
    return render(request=request, template_name="base/home.html", context=context)
    # return HttpResponse("Home")


def room(request: HttpRequest, pk: str):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i

    room = Room.objects.get(id=pk)

    context = {"room": room}
    return render(request=request, template_name="base/room.html", context=context)
    return HttpResponse("Room")


def createRoom(requset: HttpRequest):
    form = RoomForm()

    if requset.method == "POST":
        form = RoomForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect(to=home)

    context = {"form": form}
    return render(request=requset, template_name='base/room_form.html', context=context)


def updateRoom(request: HttpRequest, pk: str):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(to=home)

    context = {'form': form}
    return render(request=request, template_name="base/room_form.html", context=context)


def deleteRoom(request: HttpRequest, pk: str):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect(to=home)

    context = {"obj": room}
    return render(request=request, template_name="base/delete.html", context=context)
