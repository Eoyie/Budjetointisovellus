from db import db
from flask import session
from sqlalchemy.sql import text

def add_category(name, user_id):
    try:
        sql = text("INSERT INTO categories (name,user_id) VALUES (:name,:user_id)")
        db.session.execute(sql, {"name":name, "user_id":user_id})
        db.session.commit()
    except:
        return False
    return True

def check_category(name, user_id):
    sql = text("SELECT id FROM categories WHERE name=:name AND user_id=:user_id")
    result = db.session.execute(sql, {"name":name, "user_id":user_id})
    category_id = result.fetchone()
    if not category_id:
        return False
    return True

def get_all_categories(user_id):
    sql = text("SELECT name FROM categories WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    categories = result.fetchall()
    return categories