from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seedinsight.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import SQLAlchemy models
from models import Seed, Company, Ecozone

# Seed Registration Route
@app.route('/register_seed', methods=['GET', 'POST'])
def register_seed():
    if request.method == 'POST':
        ecozone = request.form['ecozone']
        crop_name = request.form['crop_name']
        seed_rate = float(request.form['seed_rate'])
        maturity_period = int(request.form['maturity_period'])
        yield_amount = float(request.form['yield_amount'])
        price = float(request.form['price'])
        company = request.form['company']
        availability = request.form['availability']

        new_seed = Seed(ecozone=ecozone, crop_name=crop_name, seed_rate=seed_rate,
                        maturity_period=maturity_period, yield_amount=yield_amount,
                        price=price, company=company, availability=availability)

        db.session.add(new_seed)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('seed_form.html')

# Company Registration Route
@app.route('/register_company', methods=['GET', 'POST'])
def register_company():
    if request.method == 'POST':
        company_name = request.form['company_name']
        location = request.form['location']
        contact = request.form['contact']
        specialty = request.form['specialty']

        new_company = Company(company_name=company_name, location=location,
                              contact=contact, specialty=specialty)

        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('company_form.html')

# Ecozone Registration Route (similar to the above)
# Add the route and form rendering logic here
# More pleasing content coming
# Index Route
@app.route('/')
def index():
    seeds = Seed.query.all()
    companies = Company.query.all()
    ecozones = Ecozone.query.all()
    return render_template('index.html', seeds=seeds, companies=companies, ecozones=ecozones)

if __name__ == '__main__':
    app.run(debug=True)

