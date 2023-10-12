from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from main.models import Habit
from main.paginations import ListHabitsPagination
from main.permissions import IsStaffOrOwner, IsOwner
from main.serializers import HabitsSerializer


class HabitCreateView(generics.CreateAPIView):
    """ Create view habit """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = HabitsSerializer


class HabitUpdateView(generics.UpdateAPIView):
    """ Update view habit """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    serializer_class = HabitsSerializer


class HabitsListOwnerView(generics.ListAPIView):
    """ List owner view habit """

    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListHabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitsListView(generics.ListAPIView):
    """ List public view habit """

    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListHabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitsRetrieveView(generics.RetrieveAPIView):
    """ Retrieve view habit """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    serializer_class = HabitsSerializer


class HabitDeleteView(generics.DestroyAPIView):
    """ Delete view habit """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    serializer_class = HabitsSerializer
