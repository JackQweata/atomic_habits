from rest_framework import serializers


class ExecutionTimeValidate:
    def __init__(self, estimated_time):
        self.estimated_time = estimated_time

    def __call__(self, value):
        time = dict(value).get(self.estimated_time)

        if not time:
            return
        elif time > 120:
            raise serializers.ValidationError('Время выполнения больше 120 сек')


class RelatedHabitsValidate:
    def __init__(self, enjoyable, related):
        self.enjoyable = enjoyable
        self.related = related

    def __call__(self, value):
        is_enjoyable = dict(value).get(self.enjoyable)
        related_habit = dict(value).get(self.related)

        if related_habit and is_enjoyable:
            raise serializers.ValidationError('В связанные привычки могут попадать только привычки с признаком '
                                               'приятной привычки.')


class RewardHabitsValidate:
    def __init__(self, enjoyable, reward):
        self.enjoyable = enjoyable
        self.reward = reward

    def __call__(self, value):
        is_enjoyable = dict(value).get(self.enjoyable)
        reward = dict(value).get(self.reward)

        if reward and is_enjoyable:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class HabitTimeValidate:
    def __init__(self, frequency):
        self.frequency = frequency

    def __call__(self, value):
        frequency = dict(value).get(self.frequency)

        if not frequency:
            return
        elif int(frequency) not in [1, 7]:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class RelatedHabitAction:
    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        main_habit = dict(value).get(self.related_habit)
        reward = dict(value).get(self.reward)

        if not main_habit:
            return
        elif main_habit and reward or main_habit.related_habit:
            raise serializers.ValidationError('Oдновременный выбор связанной привычки и указания вознаграждения не '
                                               'могут быть')
