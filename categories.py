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

def check_categories_exist(user_id):
    sql = text("SELECT * FROM categories WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    category = result.fetchone()
    if not category:
        return False
    return True

def get_all_categories(user_id):
    sql = text("SELECT name,id FROM categories WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    categories = result.fetchall()
    return categories

def get_category_id(name, user_id):
    sql = text("SELECT id FROM categories WHERE name=:name and user_id=:user_id")
    result = db.session.execute(sql, {"name":name, "user_id":user_id})
    category_id = result.fetchall()
    return category_id
        