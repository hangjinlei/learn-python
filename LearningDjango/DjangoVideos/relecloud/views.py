from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, "destination.html", {
        "destinations": all_destinations
    })


class DestinationDetailView(DetailView):
    model = models.Destination
    template_name = "destination_datail.html"
    content_object_name = "destination"


class DestinationCreateView(CreateView):
    model = models.Destination
    template_name = "destination_form.html"
    fields = ["name", "description"]


class DestinationUpdateView(UpdateView):
    model = models.Destination
    template_name = "destination_form.html"
    fields = ["name", "description"]


class DestinationDeleteView(DeleteView):
    model = models.Destination
    template_name = "destination_confirm_delete.html"
    success_url = reverse_lazy("destinations")
