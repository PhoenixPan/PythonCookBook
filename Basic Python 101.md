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
