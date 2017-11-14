from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from tasks.models import Task


class ServeTasks(APIView):
    """
    View for sending responses for get and post requests to the task list.
    """

    def get(self, request, username):
        """Return a list of all tasks."""
        user = User.objects.get(username=username)
        if not user:
            return NotFound('The profile does not exist')
        output = {
            'username': user.username,
            'tasks': Task.serializable.filter(user__username=username).as_dict()
        }
        return Response(output)
