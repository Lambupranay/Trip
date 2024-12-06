import os

from flask import Flask, render_template, redirect, url_for, flash
from forms import VisitInterestForm
from models import VisitInterest, db

from flask_migrate import Migrate

# Initialize Migrate


app = Flask(__name__)

import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'd2b2e7b091214f37b94d3a35a6b6c127ad3a8174ce5c4f4e')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')

# app.config['SECRET_KEY'] = 'd2b2e7b091214f37b94d3a35a6b6c127ad3a8174ce5c4f4e'  # For CSRF protection

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Using SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db.init_app(app)


migrate = Migrate(app, db)


@app.route('/')
def Home():
    return "This is Home Page"

@app.route('/submit-interest', methods=['GET', 'POST'])
def submit_interest():
    form = VisitInterestForm()
    if form.validate_on_submit():
        # Save form data to database
        interest = VisitInterest(
            name=form.name.data,
            user_id=form.user_id.data,
            phone_number=form.phone_number.data,
            willing_to_come_to_zoo=form.willing_to_come_to_zoo.data,
            willing_to_come_to_charminar=form.willing_to_come_to_charminar.data
        )
        db.session.add(interest)
        db.session.commit()
        flash('Thank you for your submission!', 'success')
        return redirect(url_for('thank_you'))
    return render_template('form_page.html', form=form)

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/view-responses')
def view_responses():
    responses = VisitInterest.query.all()
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)  # Starts the Flask development server
