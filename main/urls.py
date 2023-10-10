from django.urls import path
from main.apps import MainConfig
from main.views import *

app_name = MainConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateView.as_view(), name='create-habit'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='update-habit'),
    path('habit/delete/<int:pk>/', HabitDeleteView.as_view(), name='delete-habit'),
    path('habit/<int:pk>/', HabitsRetrieveView.as_view(), name='ret-habit'),
    path('habits/', HabitsListOwnerView.as_view(), name='list-owner-habit'),
    path('habits/public/', HabitsListView.as_view(), name='list-public-habit'),
]
