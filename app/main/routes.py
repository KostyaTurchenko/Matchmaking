from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/Home")
def home():
    #
    return render_template("main page.html")


@main.route("/about")
def about():
    render_template("about.html")