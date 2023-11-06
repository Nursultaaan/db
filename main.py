import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "123"
)
 
cur = conn.cursor()
