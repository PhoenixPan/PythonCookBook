# Basic Python 101  

Python is an interpreted language (as opposed to the compiled languages like C), which means that you will be writing and running Python scripts. 

Two of the most common Python data structures are lists and dictionaries. We will cover them briefly here.   
  
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

print list1
print list2
print list3
print list4
print list5
```
[]  
['a', 'b', 'c']  
[1, 2, 3]  
['red', 'green', 'yellow']  
['blue', 0.5, 10, 'a']  



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
