from db import db
from flask import session
from sqlalchemy.sql import text

def add_expence(price, category_id, date, notes, user_id):
    visible = True
    try:
        float(price)
        try:
            sql = text("INSERT INTO expences (price,category_id,date,notes,user_id,visible) VALUES (:price,:category_id,:date,:notes,:user_id,:visible)")
            db.session.execute(sql, {"price":price, "category_id":category_id, "date":date, "notes":notes, "user_id":user_id,"visible":visible})
            db.session.commit()
        except:
            return False
    except:
        return False
    return True

def get_all_expences(user_id):
    sql = text("SELECT price,category_id,date,notes FROM expences WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    expences = result.fetchall()
    return order_expences_by_date(expences)

def get_sum_expences(user_id):
    sql = text("SELECT SUM(price) FROM expences WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    expences_sum = result.fetchone()[0]
    return expences_sum

def order_expences_by_date(expence_list):
    expence_list.sort(key = lambda expence: expence[3], reverse=True)
    return expence_list

def get_all_in_category_list(user_id, category_id_list):
    pass