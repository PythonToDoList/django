"""Project-wide views."""
from django.http import JsonResponse, HttpResponseBadRequest
from django_todo.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def snippet_list(request):
    """
    View to list all of the available routes for this application.
    """
    routes = {
        'info': 'GET /api/v1',
        'register': 'POST /api/v1/accounts',
        'single profile detail': 'GET /api/v1/accounts/<username>',
        'edit profile': 'PUT /api/v1/accounts/<username>',
        'delete profile': 'DELETE /api/v1/accounts/<username>',
        'login': 'POST /api/v1/accounts/login',
        'logout': 'GET /api/v1/accounts/logout',
        "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
        "create task": 'POST /api/v1/accounts/<username>/tasks',
        "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
        "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
        "delete task": 'DELETE /api/v1/accounts/<username>/tasks</id>'
    }
    return JsonResponse(routes)


class ProfileView(APIView):
    def get(self, request, username, format=None):
        """Retrieve and return data for given user."""
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create new user."""
        try:
            if request.POST['password'] != request.POST['password2']:
                return JsonResponse({'error': "Passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)
            user = UserSerializer(data=request.POST)
            if user.is_valid():
                user.save()
                return JsonResponse({'msg': 'Profile created'}, status=status.HTTP_201_CREATED)
            else:
                errors = user.errors
                if 'username' in errors and errors['username'] == ['A user with that username already exists.']:
                    return JsonResponse({
                        'error': f'Username "{request.POST["username"]}" is already taken'
                    }, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return JsonResponse({'error': 'Some fields are missing'}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, username):
        """Retrieve user or raise 404."""
        return get_object_or_404(User, username=username)

    def put(self, request, username, format=None):
        """Update existing user."""
        user = self.get_object(username)
        data = dict(request.POST)
        data['username'] = data.get('username', user.username)
        data['email'] = data.get('email', user.email)
        data['password'] = data.get('password', user.password)
        serialized = UserSerializer(user, data=data)
        serialized.is_valid()
        serialized.save()
        return JsonResponse({
                'msg': 'Profile updated.',
                'profile': serialized.data
            }, status=status.HTTP_202_ACCEPTED)
        

    def delete(self, request, username, format=None):
        """Delete existing user."""
        try:
            user = self.get_object(username)
            user.delete()
        except:
            pass
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)