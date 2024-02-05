from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Paste
from django.views.generic.detail import DetailView
from django.views.generic .list import ListView
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.
class PasteCreate(CreateView):
    model=Paste
    fields=['text','name']
    
class PasteDetail(DetailView):
    model=Paste
    template_name="pastebin/paste_detail.html"
    
class PasteList(ListView):
    model = Paste
    template_name = "pastebin/paste_list.html"
    queryset=Paste.objects.all()
    context_object_name='queryset'
class PasteUpdate(UpdateView):
    model = Paste
    template_name ='pastebin/paste_detail.html'
    fields= ['text','name']
class PasteDelete(DeleteView):
    model = Paste
    template_name='pastebin/paste_confirm_delete.html' 
    success_url = reverse_lazy('pastebin_paste_list')
