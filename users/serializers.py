from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        if not validated_data.get('email') or not validated_data.get('password'):
            raise ValidationError('Не правленая форма записи')

        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])

        user.is_active = True
        user.save()
        return user
