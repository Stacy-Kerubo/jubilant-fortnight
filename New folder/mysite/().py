# coding: utf-8
from main.models import Item,ToDoList
ls=ToDoList.objects.get(id=3)
ls.item_set.create(text="Not Showing",complete=True)
