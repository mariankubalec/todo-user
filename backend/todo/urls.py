from django.urls import path
from .views import (
    AddTodoView,
    ListTodoView,
)

urlpatterns = [
    path('add', AddTodoView.as_view()),
    path('list', ListTodoView.as_view()),
]