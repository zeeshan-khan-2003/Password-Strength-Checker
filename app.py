from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using session and flash messages

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to evaluate the password strength
def check_password_strength(password):
    score = 0
    if len(password) < 8:
        score += 1
        return "Weak: Password too short!", "red"
    if not any(char.isupper() for char in password):
        score += 1
        return "Weak: Add at least one uppercase letter!", "red"
    if not any(char.islower() for char in password):
        score += 1
        return "Weak: Add at least one lowercase letter!", "red"
    if not any(char.isdigit() for char in password):
        score += 1
        return "Weak: Add at least one number!", "red"
    if not any(char in string.punctuation for char in password):
        score += 1
        return "Weak: Add at least one special character!", "red"
    
    if score <= 2:
        return "Medium: Consider improving the password", "yellow"
    elif score <= 4:
        return "Strong: Good password!", "green"
    else:
        return "Strong: Excellent password!", "green"

# Function to suggest improvements for weak passwords
def suggest_improvements(password):
    improvements = []
    if len(password) < 8:
        improvements.append("Make it at least 8 characters long.")
    if not any(char.isupper() for char in password):
        improvements.append("Add an uppercase letter.")
    if not any(char.islower() for char in password):
        improvements.append("Add a lowercase letter.")
    if not any(char.isdigit() for char in password):
        improvements.append("Include numbers.")
    if not any(char in string.punctuation for char in password):
        improvements.append("Use special characters.")
    return improvements

# Routes for Login and Register pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you can implement logic to authenticate user
        if username == "admin" and password == "admin":  # Dummy check for now
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Please try again.", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you can add logic to save the user data into a database
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/generate', methods=['POST'])
def generate():
    password = generate_password()
    return render_template('index.html', generated_password=password)

@app.route('/check_strength', methods=['POST'])
def check_strength():
    password = request.form['password']
    result, color = check_password_strength(password)
    suggestions = suggest_improvements(password)
    return render_template('index.html', password_strength=result, color=color, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
