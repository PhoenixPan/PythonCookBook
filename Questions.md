""A value is trying to be set on a copy of a slice from a DataFrame."
```
trip = trip.ix[:least]
trip['eta'] = pd.Series(eta, index=trip.index)

# change to: will resolve the issue. Why?
trip = trip.ix[:least].copy()
```
Because you are now manipulating a copy, a new instance.
