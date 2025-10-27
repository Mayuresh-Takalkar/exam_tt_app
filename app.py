from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User

app = Flask(__name__)
app.secret_key = "secret_key_123"

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables + Insert predefined users once
with app.app_context():
    db.create_all()
    if not User.query.first():
        db.session.add(User(batch="batchA", password="1234"))
        db.session.add(User(batch="batchB", password="1234"))
        db.session.commit()
        print("✅ Default users added to database")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        batch = request.form['batch']
        password = request.form['password']

        user = User.query.filter_by(batch=batch, password=password).first()

        if user:
            session['user'] = user.batch
            flash('Login successful!', 'success')
            return redirect(url_for('tt'))
        else:
            flash('Invalid credentials', 'error')

    return render_template('login.html')

@app.route('/guide')
def guide():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('guide.html')

@app.route('/tt')
def tt():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('tt.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
