from django.db import models
from users.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    is_urgent = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.assignee.name} {self.title}'
