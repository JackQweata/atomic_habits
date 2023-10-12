from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """ Регистрация пользователя  """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    