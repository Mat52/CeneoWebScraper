from app import app
from flask import render_template
@app.route("/")
@app.route("/index")
def index():
    return render_template("main.html")

@app.route("/extraction")
def extraction():
    return render_template("extraction.html")

@app.route("/productlist")
def productlist():
    return render_template("productlist.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/author")
def author():
    return render_template("author.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/name/", defaults={"name": "Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"