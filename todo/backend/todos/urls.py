from django.urls import path
from .views import ListTodo, DetailTodo, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]
