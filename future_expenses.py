from db import db
from flask import session
from sqlalchemy.sql import text

def check_price(price):
    if price.isnumeric():
        return True
    return False

def add_future_expense(price, category_id, notes, user_id):
    visible = True
    try:
        sql = text("INSERT INTO future_expenses \
                    (price,category_id,notes,user_id,visible) \
                    VALUES \
                    (:price,:category_id,:notes,:user_id,:visible)")
        db.session.execute(sql, {"price":price, "category_id":category_id,
                                "notes":notes, "user_id":user_id,
                                "visible":visible})
        db.session.commit()
    except:
        return False
    return True

