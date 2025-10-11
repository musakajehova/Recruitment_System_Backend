from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser,person, jobs

User = get_user_model()

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'surname']

class 