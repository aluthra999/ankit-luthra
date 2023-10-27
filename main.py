from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os

my_email = "pythonsmtpudemy@gmail.com"
app_password = "cjrxivkavqvbtqwn"

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "thiskeyisverysecret"
# SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyInfo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress warnings

db = SQLAlchemy(app)

current_year = datetime.now().year


# Define the Skills table


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    skills = db.Column(db.String(255), unique=True, nullable=False)

# Define Programming Languages table


class ProgrammingLanguages(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    programming_languages = db.Column(
        db.String(255), unique=True, nullable=False)

# Define Languages table


class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    languages = db.Column(db.String(255), unique=True, nullable=False)

# Define Intrest table


class Intrest(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
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

# Define Projects


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    project_name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    image_filename = db.Column(db.String(255))

    def image_url(self):
        return url_for('static', filename='images/' + self.image_filename)


# Create the database and the table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('index.html', year=current_year)


@app.route("/resume")
def resume():
    # Retrieve data from the 'Info' table
    skills = Skills.query.all()
    programming_languages = ProgrammingLanguages.query.all()
    languages = Languages.query.all()
    intrests = Intrest.query.all()
    education_data = Education.query.all()
    courses_data = Courses.query.all()
    work_experience_data = WorkExperience.query.all()
    return render_template('resume.html',
                           year=current_year,
                           skills=skills,
                           programming_languages=programming_languages,
                           languages=languages,
                           intrests=intrests,
                           education_data=education_data,
                           courses_data=courses_data,
                           work_experience_data=work_experience_data
                           )


@app.route("/projects")
def projects():
    all_projects = Projects.query.all()
    return render_template('projects.html', year=current_year, all_projects=all_projects)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    if name and email and phone and message:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject: New message from {name} on Blog Site\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                )
            success_message = "Your message has been sent!"
            return render_template("contact.html", success_message=success_message, year=current_year)
        except Exception as e:
            error_message = "There was an error sending your message. Please try again later."
            print(f"Email sending error: {str(e)}")
            return render_template("contact.html", error_message=error_message, year=current_year)
    else:
        error_message = "Please fill out all the details"
        return render_template('contact.html', error_message=error_message, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
