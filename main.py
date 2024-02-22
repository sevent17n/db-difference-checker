import psycopg2



conn1 = psycopg2.connect(
    host="host1",
    user="user1",
    password="password1",
    database="database1",
)


conn2 = psycopg2.connect(
   host="host2",
   user="user2",
   password="password2",
   database="database2",
)


cur1 = conn1.cursor()
cur2 = conn2.cursor()


cur1.execute("SELECT id, status_review FROM orders")
rows1 = cur1.fetchall()

with open("different_orders.txt", "w") as file:
    for row1 in rows1:
        id, status_review = row1

       
        cur2.execute(
            "SELECT status_review FROM orders WHERE id = %s",
            (id,)
        )
        row2 = cur2.fetchone()

      
        print(row2[0],status_review)
        if row2 and status_review != row2[0]:
            file.write(f"Different ID: {id}\n  status_review {status_review}\n")


cur1.close()
cur2.close()
conn1.close()
conn2.close()
