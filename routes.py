from flask import redirect, render_template, request, session
from app import app
import users, categories, expences, budgets

@app.route("/")
def index():
    if session.get("logged_in"):
        user_id = session.get("user_id")
        username = users.username(user_id)
        user_expences = expences.get_this_month_expences_in_category_list(user_id)
        expences_sum = expences.get_this_month_sum_expences(user_id)
        return render_template("home.html", message=username, expences=user_expences, expences_sum=expences_sum)
    return render_template("index.html")

@app.route("/home")
def home():
    if session.get("logged_in"):
        user_id = session.get("user_id")
        username = users.username(user_id)
        user_expences = expences.get_this_month_expences_in_category_list(user_id)
        expences_sum = expences.get_this_month_sum_expences(user_id)
        return render_template("home.html", message=username, expences=user_expences, expences_sum=expences_sum)
    return render_template("error.html", message="Et ole kirjautunut sisään!")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        username = users.username(session.get("user_id"))
        return render_template("home.html", message=username)
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/home")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    if session.get("logged_in"):
        users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("logged_in"):
        username = users.username(session.get("user_id"))
        return render_template("home.html", message=username)
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/home")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/new_expence", methods=["GET", "POST"])
def new_expence():
    if not session.get("logged_in"):
        return render_template("error.html", message="Et ole kirjautunut sisään!")
    if request.method == "GET":
        if categories.check_categories_exist(session.get("user_id")):
            user_categories = categories.get_all_categories(session.get("user_id"))
            return render_template("new.html", categories=user_categories)
        else:
            return render_template("error.html", message="Lisää ensin kategoria asetuksista")
    if request.method == "POST":
        price = request.form["price"]
        date = request.form["date"]
        category_id  = request.form["category"]
        notes = request.form["notes"]
        if expences.add_expence(price, category_id, date, notes, session.get("user_id")):
            return redirect("/home")
        else:
            return render_template("error_logged_in.html", message="Menon lisääminen ei onnistunut")
    
@app.route("/categories", methods=["GET", "POST"])
def manage_categories():
    if not session.get("logged_in"):
        return render_template("error.html", message="Et ole kirjautunut sisään!")
    if request.method == "GET":
        user_categories = categories.get_all_categories(session.get("user_id"))
        return render_template("categories.html", categories=user_categories)
    if request.method == "POST":
        name = request.form["name"]
        if categories.add_category(name, session.get("user_id")):
            return redirect("/categories")
        else:
            return render_template("error_logged_in.html", message="Kategorian lisäys ei onnistunut")
    
@app.route("/budgets", methods=["GET", "POST"])
def manage_budgets():
    if not session.get("logged_in"):
        return render_template("error.html", message="Et ole kirjautunut sisään!")
    if request.method == "GET":
        user_budgets = budgets.get_all_budgets(session.get("user_id"))
        return render_template("budget.html", budgets=user_budgets)
    if request.method == "POST":
        budget = request.form["budget"]
        month = request.form["month"]
        notes = request.form["notes"]
        if budgets.add_budget(budget, month, notes, session.get("user_id")):
            return redirect("/budgets")
        else:
            return render_template("error_logged_in.html", message="Budjetin lisäys ei onnistunut")