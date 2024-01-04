from flask import redirect, render_template, request, session
from app import app
import users, categories, expenses, budgets

@app.route("/")
def index():
    if session.get("logged_in"):
        user_id = session.get("user_id")
        username = users.username(user_id)
        user_expenses = expenses.get_this_month_expenses_by_category(user_id)
        expenses_sum = expenses.get_this_month_sum_expenses(user_id)
        user_budget = budgets.this_month_budget(user_id)
        if user_budget:
            if expenses_sum:
                budget_remaining = user_budget.amount - expenses_sum
            else:
                budget_remaining = user_budget.amount
        else:
            budget_remaining = None
        return render_template("home.html",
                                message=username,
                                expenses=user_expenses,
                                expenses_sum=expenses_sum,
                                budget=user_budget,
                                budget_remaining=budget_remaining)
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return render_template("error_logged_in.html",
                                message="Olet jo kirjautunut sisään.")
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        return render_template("error.html",
                                message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    if session.get("logged_in"):
        users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("logged_in"):
        return render_template("error_logged_in.html",
                                message="Olet jo kirjautunut sisään.")
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if not users.check_valid_username(username):
            return render_template("error.html",
                                   message="Käyttäjänimen tulee sisältää vain\
                                    aakkosia.")
        if not users.check_register_passwords(password1, password2):
            return render_template("error.html", message="Salasanat eroavat")
        if not users.check_if_username_free(username):
            return render_template("error.html",
                                message="Annettu käyttäjänimi on jo käytössä")
        if users.register(username, password1):
            return redirect("/")
        return render_template("error.html",
                                message="Rekisteröinti ei onnistunut")

@app.route("/new_expense", methods=["GET", "POST"])
def new_expense():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    
    user_id = session.get("user_id")
    if request.method == "GET":
        if categories.check_categories_exist(user_id):
            user_categories = categories.get_all_categories(user_id)
            return render_template("new.html", categories=user_categories)
        return render_template("error_logged_in.html",
                                message="Lisää ensin kategoria")
    if request.method == "POST":
        price = request.form["price"]
        date = request.form["date"]
        category_id  = request.form["category"]
        notes = request.form["notes"]
        if expenses.add_expense(price, category_id, date, notes, user_id):
            return redirect("/")
        return render_template("error_logged_in.html",
                                message="Menon lisääminen ei onnistunut")

@app.route("/view_expenses", methods=["GET", "POST"])
def view_expenses():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    user_id = session.get("user_id")
    if request.method == "GET":
        if expenses.check_expenses_exist(user_id):
            user_expenses = expenses.get_all_expenses(user_id)
            return render_template("view_expenses.html", expenses=user_expenses)
        return render_template("error_logged_in.html",
                                message="Lisää ensin meno")
    if request.method == "POST":
        price = request.form["price"]
        date = request.form["date"]
        category_id  = request.form["category"]
        notes = request.form["notes"]
        if expenses.add_expense(price, category_id, date, notes, user_id):
            return redirect("/")
        return render_template("error_logged_in.html",
                                message="Menon lisääminen ei onnistunut")

@app.route("/delete_expense", methods=["GET", "POST"])
def delete_expense():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    user_id = session.get("user_id")
    expense_id = request.args.get("id")
    if expenses.delete_from_view(user_id, expense_id):
        return redirect("/view_expenses")
    return render_template("error_logged_in.html",
                            message="Menon poistaminen ei onnistunut")

@app.route("/categories", methods=["GET", "POST"])
def manage_categories():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    user_id = session.get("user_id")
    if request.method == "GET":
        user_categories = categories.get_all_categories(user_id)
        return render_template("categories.html", categories=user_categories)
    if request.method == "POST":
        if request.form["action"] == "Lisaa kategoria":
            name = request.form["name"]
            if categories.add_category(name, user_id):
                return redirect("/categories")
            return render_template("error_logged_in.html",
                                    message="Kategorian lisäys ei onnistunut")
        category_id = request.form["category"]
        if categories.delete_from_view(user_id, category_id):
            if expenses.delete_all_type_from_view(user_id, category_id):
                return redirect("/categories")
        return render_template("error_logged_in.html",
                                message="Kategorian poisto ei onnistunut")

@app.route("/budgets", methods=["GET", "POST"])
def manage_budgets():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    user_id = session.get("user_id")
    if request.method == "GET":
        user_budgets = budgets.get_all_budgets(user_id)
        return render_template("budget.html", budgets=user_budgets)
    if request.method == "POST":
        budget = request.form["budget"]
        month = request.form["month"]
        if not budget.isnumeric():
            return render_template("error_logged_in.html",
                message="Budjetin lisäys ei onnistunut: \
                        budjetti pitää olla positiivinen kokonaisluku")
        if not budgets.check_month(month):
            return render_template("error_logged_in.html",
                    message="Budjetin lisäys ei onnistunut: vuosi liian suuri")
        if budgets.add_budget(budget, month, user_id):
            return redirect("/budgets")
        return render_template("error_logged_in.html",
                                message="Budjetin lisäys ei onnistunut")

@app.route("/delete_budget", methods=["GET","POST"])
def delete_budget():
    if not session.get("logged_in"):
        return render_template("error.html",
                               message="Et ole kirjautunut sisään!")
    user_id = session.get("user_id")
    budget_id = request.args.get("id")
    if budgets.delete_from_view(user_id, budget_id):
        return redirect("/budgets")
    return render_template("error_logged_in.html",
                            message="Budjetin poistaminen ei onnistunut")
