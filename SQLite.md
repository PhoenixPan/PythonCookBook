# Create SQLite tables in Python
```
import sqlite3
conn = sqlite3.connect('example.db')
conn = sqlite3.connect(":memory:")    # create database in RAM

cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE tweets_table (
                      screen_name TEXT,
                      created_at TEXT,
                      retweet_count INTEGER,
                      favorite_count INTEGER,
                      text TEXT
                  )""")

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)") # Insecure
cursor.execute("INSERT INTO tweets_table VALUES (?, ?, ?, ?, ?)", (row['screen_name'], row['created_at'], row['retweet_count'], row['favorite_count'], row['text']))

# Save the changes using "commit"
conn.commit()

# Close the connection if we are done with it. Any changes have not been committed will be lost.
conn.close()
```

```
# Vulnerable to SQL injection attack!
symbol = 'RHAT'
cursor.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol) 

# Use
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
```

(https://docs.python.org/2/library/sqlite3.html)

#Create DataFrame from SQLite
```
conn = sqlite3.connect(file_path)
cursor = conn.cursor()
vdf = pd.DataFrame(columns = ['vid', 'tmstmp', 'lat', 'lon',  'hdg', 'pid', 'rt', 'des', 'pdist', 'spd', 'tablockid', 'tatripid'])
vdf = pd.read_sql_query("SELECT * FROM vehicles WHERE vid IS NOT NULL", conn)
print vdf.loc[:,'vid']
```

(http://www.datacarpentry.org/python-ecology-lesson/08-working-with-sql)

# Manipulate datatype
```
vdf[['vid', 'hdg', 'pid', 'pdist', 'spd', 'tatripid']] = vdf[['vid', 'hdg', 'pid', 'pdist', 'spd', 'tatripid']].apply(pd.to_numeric)
vdf[['vid', 'hdg', 'pid', 'pdist', 'spd', 'tatripid']] = vdf[['vid', 'hdg', 'pid', 'pdist', 'spd', 'tatripid']].astype(int)

vdf['tmstmp'] = pd.to_datetime(vdf['tmstmp'])
vdf['vid'] = vdf['vid'].astype(int)

pdf['dly'] = pdf['dly'].astype(bool) # empty = False, otherwise = True
```


(http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_numeric.html)
(https://pandas-docs.github.io/pandas-docs-travis/generated/pandas.to_numeric.html)

# Organiza data
```
my_group = vdf.groupby(['vid', 'pid', 'des', 'rt'])
my_group.count()
my_group.mean()

for g in my_group.groups:
    print g

my_group.get_group('6653')

my_df = my_df.sort_index(by=['Peak', 'Weeks'], ascending=[True, False])
```

Find all unique value in a column:  
```
print df.column_name.unique()
```

```
def split_trips(df):
    """ Splits the dataframe of vehicle data into a list of dataframes for each individual trip.
    Args:
        df (pd.DataFrame): A dataframe containing TrueTime bus data
    Returns:
        (list): A list of dataframes, where each dataFrame contains TrueTime bus data for a single bus running a
    """

    all_trips = []
    group_by_trip = df.groupby(['vid', 'pid', 'des', 'rt'])  # Group data

    for g in group_by_trip.groups:         # Iterate each group, get indexes
        trip = group_by_trip.get_group(g)  # Using the indexes to get the DataFrame
        trip.set_index(['tmstmp'])         # Set index
        trip = trip.sort_values(by=['tmstmp','pdist'], ascending=[True, True])  # Sort/rank the rows in the df
        last_pdist = 0
        start = 0
        end = 0
        for index, row in trip.iterrows():
            if last_pdist <= row['pdist']:
                last_pdist = row['pdist']
                end += 1
            else:
                all_trips.append(trip[start:end])
                last_pdist = row['pdist']
                start = end
                end += 1
        all_trips.append(trip[start:end])

    return all_trips
```
