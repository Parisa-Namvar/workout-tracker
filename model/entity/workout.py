class Workout:
    def __init__(self, id, user_id, name, sets, reps, datetime, weight=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.sets = sets
        self.reps = reps
        self.datetime = datetime
        self.weight = weight

def __repr__(self):
    return (f"{self.__dict__}")
