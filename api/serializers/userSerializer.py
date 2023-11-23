from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import IncubatorDevice, IncubatorSetting

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        
        if 'password' in validated_data:
            password = validated_data['password']
            instance.set_password(password)

        instance.save()
        return instance
