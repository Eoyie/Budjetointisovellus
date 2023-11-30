 CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
    );
CREATE TABLE categories (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    grouping INTEGER, 
    user_id INTEGER REFERENCES users
    visible BOOLEAN
    );
CREATE TABLE expences (
    id SERIAL PRIMARY KEY,
    price INTEGER, 
    category_id INTEGER REFERENCES categories, 
    date DATE, 
    notes TEXT, 
    user_id INTEGER REFERENCES users
    visible BOOLEAN
    );
CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    amount INTEGER,
    date DATE,
    visible BOOLEAN
    );