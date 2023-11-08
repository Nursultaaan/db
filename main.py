import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "123456" #v1.2
)
 
cur = conn.cursor()
