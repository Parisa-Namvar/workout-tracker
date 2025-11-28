import sqlite3
from model.entity.workout import Workout

class WorkoutRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/workout.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save (self ,workout):
        self.connect()
        self.cursor.execute("insert into workouts (user_id, name, sets, reps,"
                            " datetime, weight) values (?,?,?,?,?,?)",
                            [workout.user_id, workout.name,workout.sets,
                             workout.reps,workout.datetime,workout.weight])
        self.connection.commit()
        self.disconnect()

    def update (self ,workout):
        self.connect()
        self.cursor.execute("update workouts set name=?, sets=?, reps=?, datetime=?, weight=? where id=?",
                            [workout.name,workout.sets,workout.reps,
                             workout.datetime,workout.weight,workout.id])
        self.connection.commit()
        self.disconnect()

    def delete (self ,id):
        self.connect()
        self.cursor.execute("delete from workouts where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from workouts")
        workout_list = [ Workout (*workout) for workout in self.cursor.fetchall()]
        self.disconnect()
        return workout_list

    def find_one(self ,id):
        self.connect()
        self.cursor.execute("select * from workouts where id=?",[id])
        workout_list = [Workout(*workout) for workout in self.cursor.fetchall()]
        self.disconnect()
        return workout_list
