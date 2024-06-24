from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    car_model = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_listed = db.Column(db.DateTime, default=datetime.utcnow)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.Text, nullable=True)

@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@app.route('/list-car', methods=['GET', 'POST'])
def list_car():
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        car_model = request.form['car_model']
        description = request.form['description']
        new_car = Car(owner_name=owner_name, car_model=car_model, description=description)
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('list_car.html')

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        appointment_date = request.form['appointment_date']
        message = request.form['message']
        new_appointment = Appointment(name=name, email=email, phone=phone, 
                                      appointment_date=datetime.strptime(appointment_date, '%Y-%m-%d'), 
                                      message=message)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('home'))
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

@app.route('/book-appointment', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        appointment_date = request.form['appointment_date']
        message = request.form['message']
        new_appointment = Appointment(name=name, email=email, phone=phone, 
                                      appointment_date=datetime.strptime(appointment_date, '%Y-%m-%d'), 
                                      message=message)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('appointments'))
    return render_template('book_appointment.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

