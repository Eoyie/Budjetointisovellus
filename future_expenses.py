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

def check_future_expenses_exist(user_id):
    sql = text("SELECT user_id FROM future_expenses WHERE user_id=:user_id \
                AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id})
    expenses = result.fetchone()
    if not expenses:
        return False
    return True

def get_all_future_expenses(user_id):
    sql = text("SELECT E.price, C.name, E.notes, E.id \
            FROM future_expenses E INNER JOIN categories C ON C.id = E.category_id \
            WHERE E.user_id=:user_id AND E.visible=TRUE \
            GROUP BY E.price, C.name, E.notes, E.id")
    result = db.session.execute(sql, {"user_id":user_id})
    expenses = result.fetchall()
    return expenses

def delete_from_view(user_id, expense_id):
    try:
        sql = text("UPDATE future_expenses SET visible=FALSE\
                        WHERE user_id=:user_id AND id=:expense_id")
        db.session.execute(sql, {"user_id":user_id, "expense_id":expense_id})
        db.session.commit()
    except:
        return False
    return True
