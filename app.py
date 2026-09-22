from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

# Intentionally hardcoded training secret.
# This is fake and exists only for the Week 6 AppSec lab.
app.secret_key = "week6-training-secret-key"

ADMIN_USERNAME = "analyst"
ADMIN_PASSWORD = "TrainingOnly-Admin-123!"


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """
    )

    cursor.execute("SELECT COUNT(*) FROM employees")

    if cursor.fetchone()[0] == 0:
        employees = [
            ("Amara Okafor", "aokafor", "Security Operations", "SOC Analyst"),
            ("Daniel Mensah", "dmensah", "Cloud Engineering", "Cloud Engineer"),
            ("Sarah Bello", "sbello", "Engineering", "Backend Developer"),
            ("Michael Adeyemi", "madeyemi", "Security", "Security Engineer"),
        ]

        cursor.executemany(
            """
            INSERT INTO employees (name, username, department, role)
            VALUES (?, ?, ?, ?)
            """,
            employees,
        )

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))

        error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", user=session["user"])


@app.route("/directory", methods=["GET", "POST"])
def directory():
    if "user" not in session:
        return redirect(url_for("login"))

    employees = []
    search = ""

    if request.method == "POST":
        search = request.form.get("username", "")

        conn = sqlite3.connect("users.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # INTENTIONALLY VULNERABLE:
        # User-controlled input is concatenated directly into SQL.
        query = (
            "SELECT id, name, username, department, role "
            "FROM employees WHERE username LIKE '%"
            + search
            + "%'"
        )

        cursor.execute(query)
        employees = cursor.fetchall()
        conn.close()

    return render_template(
        "directory.html",
        employees=employees,
        search=search,
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
