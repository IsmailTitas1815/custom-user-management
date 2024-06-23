from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'password', 'authentication_token']
        extra_kwargs = {
            'password': {'write_only': True},
            'authentication_token': {'read_only': True}
        }

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request', None)
        
        if request and request.method == 'GET':
            self.fields.pop('authentication_token')

    def create(self, validated_data):
        if 'user_type' in validated_data:
            del validated_data['user_type']
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
