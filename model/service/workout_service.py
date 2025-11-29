from model.repository.workout_repository import WorkoutRepository


class WorkoutService:
    def __init__(self):
        self.repository = WorkoutRepository

    def save (self ,workout):
        self.repository.save(workout)

    def update (self ,workout):
        self.repository.update(workout)

    def delete (self ,id):
        self.repository.delete(id)

    def find_all(self):
        self.repository.find_all()

    def find_one(self ,id):
        self.repository.find_one(id)