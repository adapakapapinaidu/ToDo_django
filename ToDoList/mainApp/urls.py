from django.urls import path
from .views import *


urlpatterns = [
    path ('<int:pk>/',DetailToDoList.as_view()),
    path('',ListTodo.as_view()),
    path('create',CreateTodo.as_view()),
    path('delete/<int:pk>',DeleteTodo.as_view())

]