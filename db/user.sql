create table if not exists users(
    id integer primary key autoincrement,
    username text,
    password text,
    first_name text,
    last_name text,
    age integer,
    register_date date,
    phone_number text,
    email text
);