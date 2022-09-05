from django.shortcuts import render
from .models import ToDoItem


def ToDoView(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, 'main.html', {'all_items': all_todo_items})


def ToDoAdd(request):
    all_todo_items = ToDoItem.objects.all()
    x = request.POST['content']
    new_item = ToDoItem(content=x)
    new_item.save()
    return render(request, 'main.html', {'all_items': all_todo_items})


def ToDoDelete(request, i):
    all_todo_items = ToDoItem.objects.all()
    y = ToDoItem.objects.get(id=i)
    y.delete()
    return render(request, 'main.html', {'all_items': all_todo_items})

