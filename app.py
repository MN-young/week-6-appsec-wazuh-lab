import sqlite3

# Intentionally vulnerable code for Week 6 AppSec lab.
# DO NOT use these patterns in a real application.

ADMIN_PASSWORD = "SuperSecretAdmin123!"

def find_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable: user input is concatenated directly into SQL.
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


if __name__ == "__main__":
    username = input("Enter username: ")
    print(find_user(username))
