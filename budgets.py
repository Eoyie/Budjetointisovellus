from db import db
from flask import session
from sqlalchemy.sql import text
from datetime import datetime

def add_budget(amount, date, notes, user_id):
    visible = True
    date = datetime.strptime(date, "%Y-%m")
    try:
        try:
            sql = text("SELECT id FROM budgets WHERE user_id=:user_id \
                            AND date=:date")
            result = db.session.execute(sql, {"user_id":user_id, "date":date})
            id = ' '.join(map(str, result.fetchone()))
            sql = text("UPDATE budgets SET amount=:amount, notes=:notes \
                       WHERE user_id=:user_id AND id=:id")
            db.session.execute(sql, {"amount":amount, "notes":notes, 
                                     "user_id":user_id, "id":id})
            db.session.commit()
        except:
            sql = text("INSERT INTO budgets (amount,date,notes,user_id,visible)\
                        VALUES (:amount,:date,:notes,:user_id,:visible)")
            db.session.execute(sql, {"amount":amount, "date":date,
                                     "notes":notes, "user_id":user_id,
                                     "visible":visible})
            db.session.commit()
    except:
        return False
    return True

def this_month_budget(user_id):
    month = datetime.now().month
    year = datetime.now().year
    try:
        sql = text("SELECT amount,date FROM budgets WHERE user_id=:user_id \
                    AND EXTRACT(MONTH FROM date)=:month AND \
                    EXTRACT(YEAR FROM date)=:year")
        result = db.session.execute(sql, {"user_id":user_id, "month":month,
                                          "year":year})
        budgets = result.fetchall()
        return budgets[0]
    except:
        return False

def get_all_budgets(user_id):
    sql = text("SELECT amount, TO_CHAR(date, 'MM-YYYY') as month, notes \
               FROM budgets WHERE user_id=:user_id \
               ORDER BY date DESC")
    result = db.session.execute(sql, {"user_id":user_id})
    budgets = result.fetchall()
    return budgets