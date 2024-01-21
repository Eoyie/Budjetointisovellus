from db import db
from flask import session
from sqlalchemy.sql import text

def add_category(name, user_id):
    visible = True
    try:
        sql = text("INSERT INTO categories (name,user_id,visible) \
                   VALUES (:name,:user_id,:visible)")
        db.session.execute(sql, {"name":name, "user_id":user_id,
                                 "visible":visible})
        db.session.commit()
    except:
        return False
    return True

def check_category_already_exists(user_id, category_name):
    sql = text("SELECT id FROM categories \
                WHERE user_id=:user_id AND name=:category_name\
                AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id, 
                                      "category_name":category_name})
    category = result.fetchone()
    if not category:
        return False
    return True
    

def check_categories_exist(user_id):
    sql = text("SELECT name FROM categories WHERE user_id=:user_id \
                AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id})
    category = result.fetchone()
    if not category:
        return False
    return True

def get_all_categories(user_id):
    sql = text("SELECT name, id FROM categories WHERE user_id=:user_id \
                AND visible=TRUE ORDER BY name")
    result = db.session.execute(sql, {"user_id":user_id})
    categories = result.fetchall()
    return categories

def get_category_id(name, user_id):
    sql = text("SELECT id FROM categories \
               WHERE name=:name and user_id=:user_id AND visible=TRUE")
    result = db.session.execute(sql, {"name":name, "user_id":user_id})
    category_id = result.fetchall()
    return category_id

def delete_from_view(user_id, category_id):
    sql = text("UPDATE categories SET visible=FALSE\
                WHERE user_id=:user_id AND id=:category_id")
    db.session.execute(sql, {"user_id":user_id, "category_id":category_id})
    db.session.commit()
