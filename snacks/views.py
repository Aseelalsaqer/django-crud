from django.db import models
from django.shortcuts import render
from .models import Snack
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

# Create your views here.


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = 'snack_list'


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = 'snack_detail'
    fields = ['title', 'purchaser', 'description']


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ['title' , 'purchaser', 'description']



class SnackUpdateView(UpdateView):
    template_name = "snack_update,html"
    model = Snack
    context_object_name = 'snack_update'
    fields = ['title', 'description']


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    context_object_name = 'snack_delete'
    success_url = reverse_lazy('snack_list')
