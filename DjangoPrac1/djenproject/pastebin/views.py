from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Paste

# Create your views here.
class PasteCreate(CreateView):
    model=Paste
    fields=['text','name']