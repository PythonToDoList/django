"""Views for the tasks."""
from datetime import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from tasks.models import Task


class AllTasks(APIView):
    """View for sending responses for get and post requests to the task list."""

    def get(self, request, username):
        """Return a list of all tasks."""
        try:
            user = User.objects.get(username=username)
            output = {
                'username': user.username,
                'tasks': Task.serializable.filter(user__username=username).as_dict()
            }
            return Response(data=output)
        except User.DoesNotExist:
            return NotFound('The profile does not exist')

    def post(self, request, username):
        """Add a new task to the task list."""
        try:
            user = User.objects.get(username=username)
            due_date = request.POST['due_date']
            new_task = Task(
                name=request.POST['name'],
                note=request.POST['note'],
                due_date=datetime.strptime(due_date, '%d/%m/%Y %H:%M:%S') if due_date else None,
                completed=request.POST['completed'],
                user=user,
            )
            new_task.save()
            return JsonResponse({'msg': 'posted'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return NotFound('The profile does not exist')
        except KeyError:
            return JsonResponse({'error': 'Some fields are missing'}, status=status.HTTP_400_BAD_REQUEST)


class SingleTasks(APIView):
    """Handle get, put, and delete operations for an individual task."""

    def get(self, request, username, id):
        """Return detail for an individual task."""
        pass

    def put(self, request, username, id):
        """Update detail for an individual task."""
        pass

    def delete(self, request, username, id):
        """Delete an individual task."""
        pass
