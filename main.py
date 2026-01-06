from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def home():
    conn = pymysql.connect(
        user="root",
        password="Akss2929!",
        unix_socket="/cloudsql/project-70309335-c83d-4b66-8d2:us-central1:root",
        database="testdb"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    html = "<h2>Users</h2><table border=1>"
    for r in rows:
        html += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    html += "</table>"

    cur.close()
    conn.close()
    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
