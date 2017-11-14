"""Model for the Task object."""
from django.db import models
from django.contrib.auth.models import User


class WithDict(models.Manager):
    """Take the queryset and render as a list of dictionaries."""

    def as_dict(self):
        """See above."""
        queryset = self.get_queryset()
        return [obj.to_dict() for obj in queryset]


DATE_FMT = '%d/%m/%Y %H:%M:%S'


class Task(models.Model):
    """Model for a task in the ToDo list."""

    name = models.CharField(max_length=280)
    note = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    objects = models.Manager()
    serializable = WithDict()

    def to_dict(self):
        """Render each task as a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'note': self.note,
            'creation_date': self.creation_date.strftime(DATE_FMT),
            'due_date': self.due_date.strftime(DATE_FMT) if self.due_date else None,
            'completed': self.completed,
            'profile_id': self.user.user_id
        }
