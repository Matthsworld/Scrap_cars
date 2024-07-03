# Scrap.Autoxona Web Application

This is a web application where users can list their scrap cars for sale, book appointments for car evaluations, and view all booked appointments. The application is built using Flask, SQLite, and Bootstrap.

## Features

- List scrap cars for sale
- View listed scrap cars
- Book appointments for car evaluations
- View all booked appointments

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/matthsworld/Scrap_cars.git
    cd Scrap_cars
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install Flask Flask-SQLAlchemy
    ```

4. Run the application:
    ```sh
    python app.py
    ```

The application will be available at `http://127.0.0.1:5000/`.

## Project Structure

Scrap_cars/
│
|
├── app.py
├── models.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── list_car.html
│ ├── appointments.html
│ └── book_appointment.html
├── static/
│ └── styles.css
└── db.sqlite3


## Usage

1. **Home Page:**
    - Displays all listed scrap cars.
    
2. **List Your Car:**
    - Navigate to `/list-car` to list a scrap car for sale by filling out a form with the owner's name, car model, and description.
    
3. **Book an Appointment:**
    - Navigate to `/book-appointment` to book an appointment for a car evaluation by filling out a form with your name, email, phone number, preferred appointment date, and an optional message.
    
4. **View Appointments:**
    - Navigate to `/appointments` to view all booked appointments.

## Deployment

To deploy this application to Heroku:

1. Create a `Procfile`:
    ```
    web: python app.py
    ```

2. Create a `requirements.txt`:
    ```sh
    Flask
    Flask-SQLAlchemy
    ```

3. Initialize a git repository, commit your code, and push it to Heroku:
    ```sh
    git init
    heroku create
    git add .
    git commit -m "Initial commit"
    git push heroku master
    ```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

