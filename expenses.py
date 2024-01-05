from db import db
from flask import session
from sqlalchemy.sql import text
from datetime import datetime

def check_price(price):
    if price.isnumeric():
        return True
    return False

def add_expense(price, category_id, date, notes, user_id):
    visible = True
    try:
        sql = text("INSERT INTO expenses \
                    (price,category_id,date,notes,user_id,visible) \
                    VALUES \
                    (:price,:category_id,:date,:notes,:user_id,:visible)")
        db.session.execute(sql, {"price":price, "category_id":category_id,
                                    "date":date, "notes":notes,
                                    "user_id":user_id,"visible":visible})
        db.session.commit()
    except:
        return False
    return True

def check_expenses_exist(user_id):
    sql = text("SELECT date FROM expenses WHERE user_id=:user_id \
                AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id})
    expenses = result.fetchone()
    if not expenses:
        return False
    return True

def get_all_expenses(user_id):
    sql = text("SELECT E.price, C.name, E.date, E.notes, E.id \
            FROM expenses E INNER JOIN categories C ON C.id = E.category_id \
            WHERE E.user_id=:user_id AND E.visible=TRUE \
            GROUP BY E.price, C.name, E.date, E.notes, E.id \
            ORDER BY E.date DESC")
    result = db.session.execute(sql, {"user_id":user_id})
    expenses = result.fetchall()
    return expenses

def get_sum_expenses(user_id):
    sql = text("SELECT SUM(price) FROM expenses \
                WHERE user_id=:user_id AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id})
    expenses_sum = result.fetchone()[0]
    return expenses_sum

def get_this_month_sum_expenses(user_id):
    month = datetime.now().month
    year = datetime.now().year
    sql = text("SELECT SUM(price) FROM expenses WHERE user_id=:user_id \
               AND EXTRACT(MONTH FROM date)=:month \
               AND EXTRACT(YEAR FROM date)=:year AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id, "month":month,
                                      "year":year})
    expenses_sum = result.fetchone()[0]
    return expenses_sum

def get_this_month_expenses_by_category(user_id):
    month = datetime.now().month
    year = datetime.now().year
    sql = text("SELECT SUM(E.price) as price,C.name \
                FROM \
                expenses E INNER JOIN categories C ON C.id = E.category_id \
                WHERE \
                E.user_id=:user_id AND EXTRACT(MONTH FROM E.date)=:month \
                AND EXTRACT(YEAR FROM E.date)=:year AND E.visible=TRUE \
                GROUP BY C.name")
    result = db.session.execute(sql, {"user_id":user_id, "month":month,
                                      "year":year})
    expenses = result.fetchall()
    return expenses

def delete_all_type_from_view(user_id, category_id):
    try:
        sql = text("UPDATE expenses SET visible=FALSE \
                    WHERE user_id=:user_id AND category_id=:category_id")
        db.session.execute(sql, {"user_id":user_id, "category_id":category_id})
        db.session.commit()
    except:
        return False
    return True

def delete_from_view(user_id, expense_id):
    try:
        sql = text("UPDATE expenses SET visible=FALSE\
                        WHERE user_id=:user_id AND id=:expense_id")
        db.session.execute(sql, {"user_id":user_id, "expense_id":expense_id})
        db.session.commit()
    except:
        return False
    return True
