## Basic operation
```
# Check 10 lines
df.head()
```

## Create DataFrame from SQLite database
```
import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect(fname)
cursor = conn.cursor()

# Create the structure of df
vdf = pd.DataFrame(columns = ['vid', 'tmstmp', 'lat', 'lon',  'hdg', 'pid', 'rt', 'des', 'pdist', 'spd', 'tablockid', 'tatripid'])

# Use SQL statement to read from the connection
vdf = pd.read_sql_query("SELECT * FROM vehicles WHERE vid<>\"\"", conn)
```

## Create DataFrame directly from .csv file
skiprows: skip the table heading
names: column names
```
df = pd.read_csv(users_filepath, skiprows = 1,
                 names=['name', 'screen_name', 'location', 'created_at',
                        'friends_count', 'followers_count',
                        'statuses_count', 'favourites_count'])
```

## Change datatype
String to numeric
```
vdf[['vid', 'hdg']] = vdf[['vid', 'hdg']].apply(pd.to_numeric)
vdf['vid'] = vdf['vid'].astype(int)
vdf[['vid', 'hdg']] = vdf[['vid', 'hdg']].astype(int)
```
Date format string to datetime
```
vdf['tmstmp'] = pd.to_datetime(vdf['tmstmp'])
```
String to boolean, empty values will be False, otherwise True
```
pdf['dly'] = pdf['dly'].astype(bool)
```

(http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_numeric.html)
(https://pandas-docs.github.io/pandas-docs-travis/generated/pandas.to_numeric.html)
(http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)

## Manipulate DataFrame
Add new column  
```
df['newCol'] = pd.Series(newColList) 
df['newCol'] = newColList?
```  
Drop column in DataFrame
Axis: "1" means column, "0" means X  
```
df = df.drop('tmrk', 1)
```
Set index (do remember to assign the new value back)
```
df = df.set_index(['tmstmp'])
df = df.set_index(['column1','column2'])
```
Sort
```
df = df.sort_values(by=['tmstmp', 'pdist'], ascending=[True, True])
```
Groupby
```
my_group = vdf.groupby(['vid', 'pid', 'des', 'rt'])

# Iterate the all the groups
for g in my_group.groups:
    df = my_group.get_group(g)

my_group.get_group('6653')
my_group.count()
my_group.mean()
```
Find all unique value in a column  
```
print df.column_name.unique()
```
Show Null values and replace them  
```
print users.isnull().values.any()  # True
users = users.fillna('')
```
#####Example   
```
def split_trips(df):
    all_trips = []
    group_by_trip = df.groupby(['vid', 'pid', 'des', 'rt'])

    for g in group_by_trip.groups:         # Iterate each group, get indexes
        trip = group_by_trip.get_group(g)  # Using the indexes to get the DataFrame
        trip = trip.sort_values(by=['tmstmp','pdist'], ascending=[True, True])  # Sort/rank the rows in the df
        trip = trip.set_index(['tmstmp']) 
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
