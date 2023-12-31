#v1.3
import psycopg2
import csv 

conn = psycopg2.connect (
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "1234567" 
)
 
cur = conn.cursor()
print("Connected successfully!") 
cur.execute("SELECT * FROM customers")
usernames = cur.fetchall()
for i in usernames:
    print(i)

filename = "users.csv"

with open(filename, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerows(usernames)

# username = input("Enter your username: ")
# if username in usernames:
#     print("Your username exist in our database")
# else:
#     print("Error! Couldn't find your username in our database.")

# def binary_search(username):
#     low = 0 
#     high = len(usernames) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = usernames[mid]

#         if guess == username:
#             print(f"Found username {username} in the database")
#             return 
#         elif guess < username:
#             low = mid + 1
#         else:
#             high = mid - 1

#     print(f"Username {username} not found in the database")

# username = input("Enter your username: ")
# print(usernames)
# binary_search(username)