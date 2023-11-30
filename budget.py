from db import db
from flask import session
from sqlalchemy.sql import text

def add_budget(user_id, amount, date, category_id=""):
    try:
        sql = text("INSERT INTO budgets (amount,date,category_id,user_id) VALUES (:amount,:date,:category_id,:user_id)")
        db.session.execute(sql, {"amount":amount, "category_id":category_id, "user_id":user_id})
        db.session.commit()
    except:
        return False
    return True

def this_month_budget(user_id):
    sql = text("SELECT amount,date FROM budgets WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    budgets = result.fetchall()
    return order_budgets_by_date(budgets)[0]

def order_budgets_by_date(budget_list):
    budget_list.sort(key = lambda budget: budget[1], reverse=True)
    return budget_list