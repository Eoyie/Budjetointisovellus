from flask import redirect, render_template, request, session
from app import app
import users, categories

@app.route("/")
def index():
    if session.get("logged_in") == True:
        username = users.username(session.get("user_id"))
        return render_template("home.html", message=username)
    return render_template("index.html")

@app.route("/home")
def home():
    if session.get("logged_in") == True:
        username = users.username(session.get("user_id"))
        return render_template("home.html", message=username)
    return render_template("error.html", message="Et ole kirjautunut sisään!")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in") == True:
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
    if session.get("logged_in") == True:
        users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("logged_in") == True:
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
    if session.get("logged_in") == False:
        return render_template("error.html", message="Et ole kirjautunut sisään!")
    if request.method == "GET":
        return render_template("new.html")
    
@app.route("/settings", methods=["GET", "POST"])
def manage_categories():
    if session.get("logged_in") == False:
        return render_template("error.html", message="Et ole kirjautunut sisään!")
    if request.method == "GET":
        user_categories = categories.get_all_categories(session.get("user_id"))
        return render_template("settings.html", categories=user_categories)
    if request.method == "POST":
        name = request.form["name"]
    if categories.add_category(name, session.get("user_id")):
        return redirect("/settings")
    else:
        return render_template("error.html", message="Kategorian lisäys ei onnistunut")