from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "username", "is_active", 'is_staff',)


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", 'password2')

    def save(self):
        username = self.validated_data["username"]
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        
        print(User.objects.filter(username='ajoy'))
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error": "Username taken"})

        if password1 != password2:
            raise serializers.ValidationError({"error": "password mismatch"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Account exist for the email. Use a different email"})
        
        account = User(username=self.validated_data['username'],email=email)
        account.set_password(password1)
        
        account.save()
        return account