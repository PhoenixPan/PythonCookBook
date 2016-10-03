## Get started
```
import matplotlib
# Use svg backend for better quality
matplotlib.use("svg")
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')
# Adjust this to fit your screen
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
```
Create a simple scatter diagram: plt.scatter(x, y)
```
plt.scatter(users_df['followers_count'], users_df['friends_count']) # both x and y are list type here
```
Or a mroe complicated one...
```
import datetime
def plot_avg_spd(df, t):
    day_time = []
    for index, row in df.iterrows():
        this_time = row['tmstmp'].to_pydatetime()
        timemark = this_time.hour * 100 + this_time.minute - this_time.minute % t
        day_time.append(timemark)
        
    df['tmrk'] = day_time
    
    time = []
    spd = []
    df = df.set_index(['tmstmp'])
    group_by_trip = df.groupby(['tmrk'])
    for g in group_by_trip.groups:
        trip = group_by_trip.get_group(g)
        trip_time = trip.index.time
        time.append(trip_time[0])
        spd.append(trip['spd'].mean())
    df = df.drop('tmrk', 1)
    return plt.scatter(time, spd)
```

Draw on plt and return a list of Line2D object
```
def plot_trip(trips, k):
    result = []
    for trip in trips:
        time = trip.index.time
        time = time.tolist()
        spd = compute_sliding_averages(trip['spd'], k).tolist()
        result.append(plt.plot(time, spd)[0])
    return result
```

```
for trip in trips:
        trip = trip.set_index('tmstmp')
        time = trip.index.time
        time = time.tolist()
        spd = compute_sliding_averages(trip['spd'], k).tolist()
        plt.plot(time, spd)
plt.show()
```
Histogram example
```
def degree_distribution(edges_df):
    dic = {}
    # Calculate the number of friends each user has
    for column, row in edges_df.iterrows():
        name = row['screen_name']
        if name in dic:
            dic[name] = int(dic[name]) + 1
        else:
            dic[name] = 1
    # Get all user count
    x = []
    for tuple in dic.iteritems():
        x.append(tuple[1])

    return matplotlib.pyplot.hist(x)
```


# Question 1
This does not work
```
time = []
spd = []
df = df.set_index(['tmstmp'])
last_time = None
group_by_trip = df.groupby(df.index.time)
for g in group_by_trip.groups:
trip = group_by_trip.get_group(g)
trip_time = trip.index.time
if len(time) == 0:
    last_time = trip_time[0]
    time.append(trip_time[0])
    spd.append(trip['spd'].mean()) 
break
plt.scatter(time, spd)
```
But this works
```
time = []
spd = []
last_time = None
df = df.set_index(['tmstmp'])
group_by_trip = df.groupby(df.index.time)
for g in group_by_trip.groups:
trip = group_by_trip.get_group(g)
trip_time = trip.index.time
if len(time) != 0:
    pass
time.append(trip_time[0])
spd.append(trip['spd'].mean())

plt.scatter(time, spd)
```
##### The result does not fit the parameter of plt.scatter
