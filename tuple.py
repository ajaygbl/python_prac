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

print('\n')
print('#####TUPLE WITH MIXED DATA TYPES######')
print('\n')

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

print('\n')
print('#####NESTED TUPLE######')
print('\n')

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


print('\n')
print('#####TUPLE UNPACKING######')
print('\n')

# tuple unpacking
a,b,c = my_tuple
print(my_tuple)


print('\n')
print('#####TUPLE index######')
print('\n')

# Tuple index
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])     
print(n_tuple[1][1])

print('\n')
print('#####Membership test######')
print('\n')

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print('a' in my_tuple)
print('b' in my_tuple)

print('g' not in my_tuple)


print('\n')
print('#####Tuple Methods#####')
print('\n')

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p')) 
print(my_tuple.index('l'))


# Deleting tuples
# Since tuple is immutable you can't delete items

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
del my_tuple


print('\n')
print('#####Changing tuple#####')
print('\n')

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])
# However, List is mutable it's element can be changed
my_tuple[3][0] = 9
print(my_tuple)
