 CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,password TEXT
    );
CREATE TABLE categories (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    grouping INTEGER, 
    user_id INTEGER REFERENCES users
    );
CREATE TABLE expences (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    amount INTEGER, 
    category_id INTEGER REFERENCES categories, 
    date TEXT, 
    notes TEXT, 
    user_id INTEGER REFERENCES users
    );