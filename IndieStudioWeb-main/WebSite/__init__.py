from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
app.config["SECRET_KEY"]='bfa633d3b9ddf8f79d9c3f49'

from WebSite import routes