from turtle import color
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/html_tips/')
def html_tips():
    return render_template("html_tips.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("full_name", "you"), color=request.args.get("color", "not here"), country=request.args.get("country", "Somewhere"))
#NOT showing default value of name and country, only color

# @app.route("/greet", methods=["POST"])
# def greet():
#     return render_template("greet.html", name=request.form.get("name", "world"))


if __name__ == "__main__":
    app.run(debug=True)



