import pymysql
import os

def main():
    print("Job started")

    conn = pymysql.connect(
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        unix_socket=f"/cloudsql/{os.environ['INSTANCE_CONNECTION_NAME']}",
        database=os.environ["DB_NAME"]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

    print("Job finished successfully")

if __name__ == "__main__":
    main()
