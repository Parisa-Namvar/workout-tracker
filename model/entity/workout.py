class Workout:
    def __init__(self, workout_id, user_id, name, sets, reps, date, weight=None):
        self.workout_id = workout_id
        self.user_id = user_id
        self.name = name
        self.sets = sets
        self.reps = reps
        self.date = date
        self.weight = weight

def __repr__(self):
    print(f"{self.__dict__}")