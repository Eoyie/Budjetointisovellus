from db import db
from flask import session
from sqlalchemy.sql import text

def add_expence(name, price, category_id, date, notes, user_id):
    try:
        float(price)
        try:
            sql = text("INSERT INTO expences (name,price,category_id,date,notes,user_id) VALUES (:name,:price,:category_id,:date,:notes,:user_id)")
            db.session.execute(sql, {"name":name, "price":price, "category_id":category_id, "date":date, "notes":notes, "user_id":user_id})
            db.session.commit()
        except:
            return False
    except:
        return False
    return True

def get_all_expences(user_id):
    sql = text("SELECT name,price,category_id,date,notes FROM expences WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    expences = result.fetchall()
    return expences

def get_sum_expences(user_id):
    sql = text("SELECT SUM(price) FROM expences WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    expences_sum = result.fetchone()[0]
    return expences_sum