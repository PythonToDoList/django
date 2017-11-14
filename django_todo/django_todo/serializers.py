"""Serializer for the User model."""
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User object."""

    class Meta:
        """Set up the model for the serializer to user."""

        model = User
        fields = ('id', 'username', 'email', 'password', 'tasks')

    def create(self, validated_data):
        """Create and return a new 'User' instance."""
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update existing 'User' instance."""
        user = instance
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        if validated_data['password'] != user.password:
            user.set_password(validated_data['password'])
        user.save()
        return user

    @property
    def data(self):
        """Scrub the password from the returned data."""
        _data = super(UserSerializer, self).data
        del _data['password']
        return _data
