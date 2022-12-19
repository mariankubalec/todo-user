from django.urls import path
from .views import (
    AddTodoView,
    ListTodoView,
    GetTodoView,
)

urlpatterns = [
    path('add', AddTodoView.as_view()),
    path('list', ListTodoView.as_view()),
    path('', ListTodoView.as_view()),
    path('<int:pk>', GetTodoView.as_view()),
]
