# Basics

Python is an interpreted language (as opposed to the compiled languages like C), which means that you will be writing and running Python scripts. Two of the most common Python data structures are lists and dictionaries.  

##### Import functions from [.py] file
```
from time_series import load_data, split_trips
```
## Lists  
  
Lists are sequences of objects that are denoted by brackets. We can  
* initialize a list by directly specifying their elements  
* these elements do not have to be the same  

```
list1 = []
list2 = ['a', 'b', 'c']
list3 = [1, 2, 3 ]
list4 = ["red", "green", "yellow"]
list5 = ["blue", 0.5, 10, 'a']
```
append, extend, and +=
```
c = [1, 2, 3]
c.extend(c) is the same as c += c 
[1, 2, 3, 1, 2, 3]
c.append(c)
[1, 2, 3, [...]]
```

```
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
print '-' * 10
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
```


### Generator expressions
Using the same list comprehensions without the brackets results in a generator expression. For example, the following generator expression generates every integer from 1 to `n`.

A generator expression is slightly different from a list in that the contents of entire list are generated on the fly as opposed to all at once. This is particularly useful when you don't need to access the entire list at once, but only need to iterate over over elements. For example, in the previous line where we counted the number of words in Shakespeare, we could have instead omitted the brackets and passed a generator expression to avoid allocating memory for the entire list. 

Without constructing the entire list, all about performance  
```
# Normal: creating a list and then sum it
num_words = sum([len(line.split()) for line in shakespeare])
print num_words
  
# Generator expression: sum each len directly  
print sum(len(line.split( )) for line in shakespeare)  
```


## Parameters
```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
# Accepted
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# Invalid
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```
https://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions  

##Dictionary
#####Creation  
```
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```
##### Basic operation
```
edges = {"A":{"B":1.0, "C":1.0}}
type(G.edges["A"]["B"]) # float

if edges.has_key(key):
    edges[key].update(value)
else:
    edges[key] = value
```

#####Iterator  
In python 2.x:  
"for word in d" is better than "for word in d.key()" which creates a list of all keys every time it processes  
"for word in d.iterkey()" go through it without creating the list  
  
In python 3.x:  
.key() is actually .iterkey()  
old .key() is now .viewkey()  

Iterate N times where N is known:
```
for i in xrange(N):
    do_something()
```

##Json
```
import json
aim = json.loads(data) # expect a string 
aim = json.loads(data) # expect an python io object
```
strict: If strict is False (True is the default), then control characters will be allowed inside strings. Control characters in this context are those with character codes in the 0-31 range, including '\t' (tab), '\n', '\r' and '\0'.  
```
jStr = json.loads(jsonString, strict=False)
```
Find all keys with the same name in JSON
```
def parse_api_response(data):
    import json
    aim = json.loads(data)   # type(aim) is dict
    result = []
    for key in aim["businesses"]:  # type(key) is dict
        result.append(str(key.values()[0]))  # type(key.values()) is list, change it to string and append
    return result
    
test = '{"businesses": [ {"url": "www.test.com"}, {"url": "www.test2.com"} ] }'
print parse_api_response(test)
```

# Datetime

```
import datetime

# Get the current time 
datetime.datetime.now()

# Get time from a datetime
my_datetime.time()

# Make a formatted string/timestamp/whatever a datetime
to_datetime()

# Get and change year/month/day/hour/minutes... from datetime
my_datetime.year
my_datetime.replace(year=2016)
my_datetime.minute
my_datetime.replace(minute=59)
```

# String
Use "r" to indicate a raw string
```
users_filepath = r'C:\Users\Alice\Documents\Jupyter\hw2\handou\users.csv'
```

# Random
Pick a random element from list/dict/etc
```
random.choice(d.keys())
random.choice(list)
```
