```
for trip in trips:
        trip = trip.set_index('tmstmp')
        time = trip.index.time
        time = time.tolist()
        spd = compute_sliding_averages(trip['spd'], k).tolist()
        plt.plot(time, spd)
plt.show()
```


# Create an additional column to group the df
```
    day_time = []
    for index, row in df.iterrows():
        this_time = row['tmstmp'].to_pydatetime()
        timemark = this_time.hour * 100 + this_time.minute - this_time.minute % t
        day_time.append(timemark)
        
#     df['tmrk'] = pd.Series(day_time, index=df.index)
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



# Why
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
