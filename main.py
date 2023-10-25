from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "thiskeyisverysecret"
# SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyInfo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress warnings

db = SQLAlchemy(app)

current_year = datetime.now().year

# Define the Info table


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    skills = db.Column(db.String(255), unique=True, nullable=False)
    programming_languages = db.Column(
        db.String(255), unique=True, nullable=False)
    languages = db.Column(db.String(255), unique=True, nullable=False)
    interests = db.Column(db.String(255), unique=True, nullable=False)


# Define the Education table
class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    from_date = db.Column(db.String(50), nullable=False)
    to_date = db.Column(db.String(50), nullable=False)
    college_name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Defiine the Online Courses


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    year_completed = db.Column(db.String(50), nullable=False)
    course_name = db.Column(db.String(255), nullable=False)
    provider = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String())
    description = db.Column(db.String(), nullable=False)

# Define Work Experience


class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    from_date = db.Column(db.String(50), nullable=False)
    to_date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255))
    description = db.Column(db.Text(), nullable=False)


# Create the database and the table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('index.html', year=current_year)


@app.route("/resume")
def resume():
    # Retrieve data from the 'Info' table
    info_data = Info.query.all()
    education_data = Education.query.all()
    courses_data = Courses.query.all()
    work_experience_data = WorkExperience.query.all()
    return render_template('resume.html', year=current_year, info_data=info_data, education_data=education_data, courses_data=courses_data, work_experience_data=work_experience_data)


@app.route("/projects")
def projects():
    return render_template('projects.html', year=current_year)


@app.route("/contact")
def contact():
    return render_template('contact.html', year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
