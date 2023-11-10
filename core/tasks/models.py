from django.db import models
from accounts.models import User

# Create your models here.


def generate_pk():
    if Task.objects.last() is not None:
        number = (Task.objects.last().id) + 1
        return f"TASK-{number}"
    else:
        return f"TASK-1"


class Task(models.Model):
    task = models.CharField(
        default=generate_pk, max_length=255, unique=True, editable=False
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reaporter"
    )
    type = models.ForeignKey(
        "TaskType", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        "TaskStatus", on_delete=models.SET_NULL, blank=True, null=True
    )
    assign_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="Assigner"
    )

    def __str__(self):
        return f"{self.task}, {self.title}"


class TaskType(models.Model):
    name = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(
        "team.Team", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TaskAssignmentHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignment_history')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks_history', blank = True, null = True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null = True, blank = True)

    def __str__(self):
        return f'{self.task.title}/{self.assigned_to.email}'
