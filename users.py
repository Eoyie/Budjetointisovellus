from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["logged_in"] = True
            return True
        else:
            return False

def logout():
    del session["user_id"]
    session["logged_in"] = False

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) \
                   VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def username(id):
    sql = text("SELECT username FROM users WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    user = result.fetchone()
    return user[0]

def check_valid_username(username):
    if username.isalpha():
        return True
    return False

def check_register_passwords(password1, password2):
    if password1 == password2:
        return True
    return False

def check_if_username_free(username):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return True
    return False