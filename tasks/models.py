from django.db import models
from django.urls import reverse

from users.models import User


class TodoListManager(models.Manager):

    def for_user(self, user):
        return self.get_queryset().filter(owner=user)


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, models.CASCADE)

    objects = TodoListManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("list", args=[self.pk])


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    todo_list = models.ForeignKey(TodoList, models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.title} due: {self.due_date if self.due_date else 'whenever' }"