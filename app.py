from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import os
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'c031a4d9ad0821356f45b34cf0303b00'

# MongoDB setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/cheakmate"
mongo = PyMongo(app)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("Login attempt:", email, password)

        user = mongo.db.users.find_one({'email': email, 'password': password})
        print("User found:", user)

        if user:
            session['email'] = user['email']
            session['role'] = user['role']
            session['username'] = user.get('username', '')

            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'student':
                return redirect(url_for('student_dashboard'))
            else:
                return render_template('login.html', error='Invalid role')
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'role' in session and session['role'] == 'student':
        username = session['username']
        issues = mongo.db.issues.find({'username': username})
        return render_template('student_dashboard.html', username=username, issues=issues)
    return redirect(url_for('login'))


@app.route('/submit_issue', methods=['GET', 'POST'])
def submit_issue():
    if 'role' not in session or session['role'] != 'student':
        return redirect(url_for('login'))

    if request.method == 'POST':
        description = request.form['description']
        location = request.form['location']
        file = request.files['photo']
        filename = ""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

        mongo.db.issues.insert_one({
            'username': session['username'],
            'description': description,
            'location': location,
            'photo': filename,
            'status': 'Pending'
        })

        flash("Issue submitted successfully")
        return redirect(url_for('student_dashboard'))

    return render_template('submit_issue.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'role' in session and session['role'] == 'admin':
        issues = mongo.db.issues.find()
        return render_template('admin_dashboard.html', issues=issues)
    return redirect(url_for('login'))


@app.route('/update_status/<issue_id>', methods=['POST'])
def update_status(issue_id):
    if 'role' in session and session['role'] == 'admin':
        new_status = request.form['status']
        mongo.db.issues.update_one({'_id': ObjectId(issue_id)}, {'$set': {'status': new_status}})
    return redirect(url_for('admin_dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
