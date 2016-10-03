# Create SQLite tables
Initialize
```
import csv
import pandas as pd
import sqlite3
conn = sqlite3.connect('example.db')  # connect to an existing database
conn = sqlite3.connect(":memory:")    # create database in RAM

cursor = conn.cursor()  # create a cursor
```
Create table
```
cursor.execute("""CREATE TABLE tweets_table (
                      screen_name TEXT,
                      created_at TEXT,
                      retweet_count INTEGER,
                      favorite_count INTEGER,
                      text TEXT
                  )""")
```
Insert a row of data
```
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)") # Insecure
cursor.execute("INSERT INTO tweets_table VALUES (?, ?, ?, ?, ?)", (row['screen_name'], row['created_at'], row['retweet_count'], row['favorite_count'], row['text']))
```
Insert rows from .csv
```
with open(csv_file) as users_csv:
    reader = csv.DictReader(users_csv)
    for row in reader:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)",(row['name'], row['screen_name'], row['location']))
```
Execute complicated queries: nothing special, just assume that you're using a normal SQL database
```
query = """SELECT users.screen_name, IFNULL(num_of_tweets, 0) FROM users LEFT JOIN
            (SELECT screen_name AS s_name, SUM(num_of_tweets) AS  num_of_tweets FROM edges JOIN
                (SELECT screen_name AS following, COUNT(text) AS num_of_tweets FROM tweets GROUP BY screen_name)
            ON friend = following GROUP BY screen_name)
            ON users.screen_name = s_name"""
return cursor.execute(query)
```
execumtmany(): Execute many statements of the same kind at the same time
```
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```
Save the changes and close connection: Close the connection if we are done with it. Any changes have not been committed will be lost.
```
conn.commit()
conn.close()
```

Avoid vulnerable statement
```
# Vulnerable to SQL injection attack!
symbol = 'RHAT'
cursor.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol) 

# Use
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
```
(https://docs.python.org/2/library/sqlite3.html)
