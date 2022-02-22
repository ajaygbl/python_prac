"""
SET is unordered collection of unique elements
SET will not allow duplicate values
SET don't support indexing & slicing
SET don't support concatenation & multiplication
There are currently two builtin set types
1) SET 2) FROZENSET

1) SET is type is mutable, the contents can be changed using methods like add(), remove()
It can't be used as dictionary key or as an element of another SET.

2) FROZENSET is immutable
It can be used as dictionary key or as an element of another set

"""


#Create set
set1=set()
set1.add(10)
print(set1)


#True is treated as 1. so 1 & True are identical elements.
set2=set([1,2,3,4,5,True])
print(set2)

#creating with curly braces
set3={1,2,'a','python'}
print(set3)
