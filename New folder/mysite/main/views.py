from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import Create_new_list

# Create your views here.
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    #item=ls.item_set.get(id=3)
    return render(response,"main/list.html",{"ls":ls})
def home(response):
    return render(response,"main/home.html",{})
def create(response):
    if response.method=="POST":
        form=Create_new_list(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
           form=Create_new_list()
    return render(response,"main/create.html",{"form":form})