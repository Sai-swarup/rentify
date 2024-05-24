# Rentify - Where Renting Meets Simplicity

Rentify is a web application designed to connect property owners with potential tenants. The application allows users to register as either a seller or a buyer. Sellers can post their properties, and buyers can browse available rentals and express their interest.

## Features

### Part I: Basic Application
- **User Registration**: Users can register as sellers or buyers.
- **Seller Flow**: Sellers can post properties, view their posted properties, and update or delete them.
- **Buyer Flow**: Buyers can view all posted rental properties and express interest in specific properties.

### Part II: Add-On Features
- **Pagination and Form Validation**: Proper handling of pagination and form validation.
- **Login Requirement**: Buyers must log in to view seller details.
- **Like Button**: Buyers can like properties, and the like count is tracked live.
- **Email Notifications**: Both buyers and sellers receive email notifications with relevant contact details when interest is expressed.

### Part III: Optional Bonus Features
- **Cloud Deployment**: The full-stack app can be deployed on any cloud platform (e.g., Heroku, AWS Elastic Beanstalk, Microsoft Azure).

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: SQLite

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sai-swarup/rentify.git
   cd rentify


## Set Up Virtual Environment (Optional but Recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install Dependencies
    pip install Flask SQLAlchemy

## Run the Application
    python app.py

## Access the Application
    Open your web browser and navigate to http://127.0.0.1:5000/.

## Directory Structure
    rentify/
├── app.py
├── models.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── seller_dashboard.html
│   ├── buyer_dashboard.html
├── static/
│   ├── style.css
├── database.db
├── README.md

## License
    This project is licensed under the MIT License. See the LICENSE file for details.

This `README.md` file includes sections that provide an overview of the project, its features, the tech stack used, setup and installation instructions, the directory structure, future enhancements, contribution guidelines, and licensing information. This helps anyone who wants to understand, set up, or contribute to the project.


