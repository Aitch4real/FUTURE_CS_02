from flask import Flask, render_template, request, redirect, url_for, session, flash
import pyotp
import os
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Dummy user database (replace with your real database)
users_db = {
    "admin": "password123"
}

# Store 2FA secrets for each user
user_2fa_secrets = {
    "admin": pyotp.random_base32()  # Random secret for 2FA (use this per user)
}

# Route for login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if the username exists and the password matches
        if username in users_db and users_db[username] == password:
            session["username"] = username
            return redirect(url_for("two_factor_auth"))
        else:
            flash("Invalid credentials, please try again.")

    return render_template("login.html")

# Route for 2FA verification
@app.route("/2fa", methods=["GET", "POST"])
def two_factor_auth():
    username = session.get("username")

    if not username:
        return redirect(url_for("login"))

    # Generate a TOTP (Time-based OTP)
    totp = pyotp.TOTP(user_2fa_secrets[username])
    code = totp.now()  # Generate the current OTP code

    if request.method == "POST":
        verification_code = request.form["verification_code"]

        # Check if the entered code matches the generated code
        if totp.verify(verification_code):
            flash("2FA successful. You are logged in!")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid verification code. Please try again.")

    return render_template("2fa.html", code=code)  # Pass the OTP code to the template

# Route for dashboard (protected area after successful login and 2FA)
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return f"Welcome to the dashboard, {session['username']}!"
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
