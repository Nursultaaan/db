import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "Customers",
    user = "postgres",
    password = "123456" #v1.2
)
 
cur = conn.cursor()
print("Connected succesfully!")
cur.execute("SELECT first_name FROM customers")
usernames = [r[0] for r in cur.fetchall()]
username = input("Enter your username: ")
if username in usernames:
    print("Your username exist in our database")
else:
    print("Error! Couldn't find your username in database.")