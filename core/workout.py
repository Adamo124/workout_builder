# core/workout.py

class Workout:
    def __init__(self, exercises):
        self.exercises = exercises

    def filter_by_muscle(self, muscle_group):
        return [ex for ex in self.exercises if ex["muscle"] == muscle_group]

    def create_workout(self, muscle_group, amount=3):
        filtered = self.filter_by_muscle(muscle_group)
        return filtered[:amount]
