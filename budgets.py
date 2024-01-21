from db import db
from flask import session
from sqlalchemy.sql import text
from datetime import datetime

def check_month(date):
    try:
        date = datetime.strptime(date, "%Y-%m")
    except:
        return False
    return True

def check_budget(budget):
    if budget.isnumeric():
        return True
    return False

def add_budget(amount, date, user_id):
    visible = True
    date = datetime.strptime(date, "%Y-%m")
    if update_budget(amount, date, user_id):
        return True
    try:
        sql = text("INSERT INTO budgets (amount,date,user_id,visible)\
                    VALUES (:amount,:date,:user_id,:visible)")
        db.session.execute(sql, {"amount":amount, "date":date,
                                 "user_id":user_id, "visible":visible})
        db.session.commit()
    except:
        return False
    return True

def this_month_budget(user_id):
    month = datetime.now().month
    year = datetime.now().year
    sql = text("SELECT amount, date, id FROM budgets WHERE user_id=:user_id \
                AND EXTRACT(MONTH FROM date)=:month AND \
                EXTRACT(YEAR FROM date)=:year AND visible=TRUE")
    result = db.session.execute(sql, {"user_id":user_id, "month":month,
                                        "year":year})
    budgets = result.fetchall()
    if budgets:
        return budgets[0]
    return False

def get_all_budgets(user_id):
    sql = text("SELECT amount, TO_CHAR(date, 'MM-YYYY') as month, id \
               FROM budgets WHERE user_id=:user_id AND visible=TRUE \
               ORDER BY date DESC")
    result = db.session.execute(sql, {"user_id":user_id})
    budgets = result.fetchall()
    return budgets

def update_budget(amount, date, user_id):
    try:
        sql = text("SELECT id FROM budgets WHERE user_id=:user_id \
                    AND date=:date")
        result = db.session.execute(sql, {"user_id":user_id, "date":date})
        budget_id = ' '.join(map(str, result.fetchone()))
        sql = text("UPDATE budgets \
                    SET amount=:amount, visible=TRUE \
                    WHERE user_id=:user_id AND id=:budget_id")
        db.session.execute(sql, {"amount":amount, "user_id":user_id, 
                                 "budget_id":budget_id})
        db.session.commit()
    except:
        return False
    return True

def delete_from_view(user_id, budget_id):
    sql = text("UPDATE budgets SET visible=FALSE\
                WHERE user_id=:user_id AND id=:budget_id")
    db.session.execute(sql, {"user_id":user_id, "budget_id":budget_id})
    db.session.commit()
