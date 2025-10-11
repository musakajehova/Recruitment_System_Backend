from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser,person, jobs
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'surname']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # create token for new user
        Token.objects.create(user=user)
        return user
    
class Serialzer