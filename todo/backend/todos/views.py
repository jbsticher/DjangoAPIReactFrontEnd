from django.views.generic import TemplateView
from rest_framework import generics
from .models import Todo
from .serializers import ToDoSerializer


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
