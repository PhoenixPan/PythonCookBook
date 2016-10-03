# Create DataFrame directly from .csv file
```
users = pd.read_csv(users_filepath, skiprows = 1,
                    names=['name', 'screen_name', 'location', 'created_at',
                           'friends_count', 'followers_count',
                           'statuses_count', 'favourites_count'])
```

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
(http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)

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
Find them in an example function   

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

Find all unique value in a column  
```
print df.column_name.unique()
```


Show Null values and replace them
```
print users.isnull().values.any()  # True
users = users.fillna('')
```
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
