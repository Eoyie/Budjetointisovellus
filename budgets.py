from db import db
from flask import session
from sqlalchemy.sql import text
from datetime import datetime

def add_budget(amount, date, notes, user_id):
    visible = True
    date = datetime.strptime(date, "%Y-%m")
    try:
        sql = text("INSERT INTO budgets (amount,date,notes,user_id,visible) VALUES (:amount,:date,:notes,:user_id,:visible)")
        db.session.execute(sql, {"amount":amount, "date":date, "notes":notes, "user_id":user_id, "visible":visible})
        db.session.commit()
    except:
        return False
    return True

def this_month_budget(user_id):
    sql = text("SELECT amount,date FROM budgets WHERE user_id=:user_id \
               AND EXTRACT(MONTH FROM date)=:month AND EXTRACT(YEAR FROM date)=:year")
    result = db.session.execute(sql, {"user_id":user_id})
    budgets = result.fetchall()
    return order_budgets_by_date(budgets)[0]

def order_budgets_by_date(budget_list):
    budget_list.sort(key = lambda budget: budget[1], reverse=True)
    return budget_list

def get_all_budgets(user_id):
    sql = text("SELECT amount,date,notes FROM budgets WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    budgets = result.fetchall()
    return order_budgets_by_date(budgets)