from WebSite import app
from WebSite.forms import RegistrationForms 
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    form=RegistrationForms()
    if form.validate_on_submit():
        pass
    return render_template("register.html",form=form)