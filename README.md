

# Password Strength Checker with User Authentication

## Description

This is a web application that allows users to generate random passwords, check the strength of their passwords, and register/login with a simple authentication system. The project is built using Flask, HTML, and CSS, with the added functionality of a password strength checker. It allows users to generate passwords, check password strength, and get suggestions for improvement.

### Key Features:
- **Password Generator**: Generates a random password that includes letters, digits, and special characters.
- **Password Strength Checker**: Evaluates the strength of a password based on length, uppercase, lowercase, numbers, and special characters.
- **User Authentication**: Provides login and registration functionality (with dummy credentials for now).
- **Suggestions for Improvement**: Suggests improvements for weak passwords.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Password-strength-checker.git
    cd Password-strength-checker
    ```

2. Create and activate a virtual environment (optional but recommended):

    **For Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **For macOS/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Running the App:

1. After installing the dependencies, run the app with the following command:

    ```bash
    python app.py
    ```

2. Visit `http://127.0.0.1:5000/` in your browser to access the application.

### Functionalities:
- **Generate Password**: On the home page, click the "Generate Password" button to generate a new random password.
- **Check Password Strength**: Enter a password and click "Check Strength" to evaluate its strength.
- **Login**: Go to the login page to authenticate using a dummy username and password ("admin").
- **Register**: Go to the registration page to create a new user (currently a dummy implementation).

---

## Folder Structure

```
your_project/
├── app.py              # Main Flask application
├── templates/
│   ├── index.html      # Home page
│   ├── login.html      # Login page
│   └── register.html   # Registration page
└── static/
    └── (CSS, JS, images, etc.)
```

---

## Requirements

- **Flask**: The web framework used to build this application.
  
To install Flask and other dependencies, run:

```bash
pip install flask
```

---

## Future Improvements

- **Database Integration**: Implement a database (e.g., SQLite) for storing user credentials (username and password) and handling login/registration.
- **Password Hashing**: Store passwords securely by hashing them (e.g., using `bcrypt` or `werkzeug.security`).
- **Enhanced User Interface**: Improve the design and responsiveness using CSS frameworks like Bootstrap or Tailwind CSS.
- **User Authentication**: Implement a more advanced user authentication system (e.g., with sessions, JWT, etc.).
- **Advanced Password Strength Evaluation**: Implement additional rules for checking password strength and include a visual progress bar to indicate password strength.

---

### Example Usage

1. **Generate a Random Password:**

   - Click the "Generate Password" button on the home page, and a password will be displayed.
  
2. **Check Password Strength:**

   - Enter any password in the "Enter Password" field and click "Check Strength" to view the password strength and suggestions for improvement.

3. **Login:**

   - Enter the username `admin` and password `admin` on the login page (for demo purposes).
  
4. **Register:**

   - Use the registration form to create a new account (currently no real validation is implemented).

---
