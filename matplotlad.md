```
for trip in trips:
        trip = trip.set_index('tmstmp')
        time = trip.index.time
        time = time.tolist()
        spd = compute_sliding_averages(trip['spd'], k).tolist()
        plt.plot(time, spd)
```
plt.show()
