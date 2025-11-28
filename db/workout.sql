create table if not exists workouts(
    id integer primary key autoincrement,
    user_id integer,
    name text,
    sets text,
    reps text,
    datetime date,
    weight double
);