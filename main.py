import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()
#create a table
# cur.execute(""" CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     signup_date DATE DEFAULT CURRENT_DATE);
#     """)
#add some data to the table
# cur.execute("""INSERT INTO users (name, email) VALUES
#             ('Naomi Smith', 'naomi.smith@example.com'),
#             ('Devon Blake', 'devon.blake@example.com'); """)

# conn.commit()
#update data in the table
# cur.execute("""UPDATE users SET email = 'naomi.smith@newdomain.com' WHERE email = 'naomi.smith@example.com';""")
# conn.commit()

#insert bad data to test constraints
# cur.execute("""INSERT INTO users (name, email) VALUES
#             ('Alex Johnson', 'alexo.johnson@example.com');""")
#delete bad data
cur.execute("""DELETE FROM users WHERE email = 'alexo.johnson@example.com';""")
conn.commit()


cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())

conn.close()