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

def check_categories_exist(user_id):
    sql = text("SELECT name FROM categories WHERE user_id=:user_id")
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
    sql = text("SELECT id FROM categories \
               WHERE name=:name and user_id=:user_id")
    result = db.session.execute(sql, {"name":name, "user_id":user_id})
    category_id = result.fetchall()
    return category_id
        
def group_by_categories(expense_list, user_id):
    categories = get_all_categories(user_id)
    print(categories, "\n", expense_list)