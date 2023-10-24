from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "thiskeyisverysecret"

current_year = datetime.now().year


@app.route("/")
def home():
    return render_template('index.html', year=current_year)


@app.route("/resume")
def resume():
    return render_template('resume.html', year=current_year)


@app.route("/projects")
def projects():
    return render_template('projects.html', year=current_year)


@app.route("/contact")
def contact():
    return render_template('contact.html', year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
