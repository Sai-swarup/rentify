from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(200))
    is_seller = db.Column(db.Boolean)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    area = db.Column(db.String(100))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    nearby = db.Column(db.String(200))
    description = db.Column(db.String(500))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        password = generate_password_hash(request.form['password'])
        is_seller = request.form.get('is_seller') == 'on'

        new_user = User(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password, is_seller=is_seller)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_seller'] = user.is_seller
            return redirect(url_for('seller_dashboard') if user.is_seller else url_for('buyer_dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('is_seller', None)
    return redirect(url_for('index'))

@app.route('/seller_dashboard', methods=['GET', 'POST'])
def seller_dashboard():
    if 'user_id' not in session or not session.get('is_seller'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        area = request.form['area']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        nearby = request.form['nearby']
        description = request.form['description']
        owner_id = session['user_id']

        new_property = Property(area=area, bedrooms=bedrooms, bathrooms=bathrooms, nearby=nearby, description=description, owner_id=owner_id)
        db.session.add(new_property)
        db.session.commit()

    properties = Property.query.filter_by(owner_id=session['user_id']).all()
    return render_template('seller_dashboard.html', properties=properties)

@app.route('/buyer_dashboard')
def buyer_dashboard():
    if 'user_id' not in session or session.get('is_seller'):
        return redirect(url_for('login'))

    properties = Property.query.all()
    return render_template('buyer_dashboard.html', properties=properties)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
