from db import db
from flask import session
from sqlalchemy.sql import text

def add_expence(name, price, category_id, date, notes, user_id):
    try:
        print((name, price, category_id, date, notes, user_id))
        sql = text("INSERT INTO expences (name,price,category_id,date,notes,user_id) VALUES (:name,:price,:category_id,:date,:notes,:user_id)")
        db.session.execute(sql, {"name":name, "price":price, "category_id":category_id, "date":date, "notes":notes, "user_id":user_id})
        db.session.commit()
    except:
        return False
    return True

def get_all_expences(user_id):
    sql = text("SELECT name,price,category_id,date,notes FROM expences WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    expences = result.fetchall()
    return expences