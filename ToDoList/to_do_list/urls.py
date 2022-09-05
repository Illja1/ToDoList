from django.urls import path
from .views import ToDoAdd, ToDoDelete, ToDoView

urlpatterns = [
    path('', ToDoView),
    path('ToDoAdd/', ToDoAdd),
    path('ToDoDelete/<int:i>/', ToDoDelete)
]