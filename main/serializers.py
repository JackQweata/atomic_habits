from rest_framework import serializers
from main.models import Habit
from main.validators import *


class HabitsRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
        validators = [
            ExecutionTimeValidate(estimated_time='estimated_time'),
            RelatedHabitsValidate(enjoyable='is_enjoyable', related='related_habit'),
            RewardHabitsValidate(enjoyable='is_enjoyable', reward='reward'),
            HabitTimeValidate(frequency='frequency'),
            RelatedHabitAction(related_habit='related_habit', reward='reward')
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        habit = Habit.objects.create(**validated_data)
        return habit
