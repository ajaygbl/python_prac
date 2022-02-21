"""
--> Tuple objects are immutable
--> lists are enclosed with ([])
--> tuples are enclosed with (())
--> Tuples allow lists as its element
--> Tuples support nested tuples

"""

print('#####creating tuple######')
print('\n')

#creating tuple
tup1 = (10,20,'python')
print(tup1)

tup2 = 10,20,30,'hello'
print(tup2)

print('\n')
print('#####creating tuple from list######')
print('\n')

#creating tuple from list
tup3 = tuple([10,20,'python'])
print(tup3)

print('\n')
print('#####creating tuple with single element######')
print('\n')

#creating tuple with single element
tup4 = (2,)
print(type(tup4))

tup5 = (2)
print(type(tup5))

