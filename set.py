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


print('#Create set')
print('\n')

set1=set()
set1.add(10)
print(set1)

print('\n')
print('#True is treated as 1. so 1 & True are identical elements.')
print('\n')

set2=set([1,2,3,4,5,True])
print(set2)

print('\n')
print('#creating with curly braces')
print('\n')

set3={1,2,'a','python'}
print(set3)

print('\n')
print('#in & not in')
print('\n')

set3={1,2,3,'python','all'}

print('python' in set3)
print('ruby' not in set3)
print('golang' in set3)

print('\n')
print('#Removing Duplicates from list')
print('\n')

list1=[10,20,10,30,40,20,50,60,70]
list1=list(set(list1))
print(list1)

str='pythonpython'
str_s=set(str)
print(str_s)
str=''.join(str_s)
print(str)

print('\n')
print('#Set Builin functions')
print('\n')

set1={1,2,3}
set1.add(4) #add takes only one element
print(set1)

set1.remove(3) #if you try to remove non exist element it throws error
print(set1)

set1.discard(1) #if you try to remove non exist element it doesn't throw error 
print(set1)

set1.pop() #it doesn't take any argument. randomly delete elements
print(set1)

print('\n')
print('#set union functions')
print('\n')

#union - it will return all values from two sets except duplicates
set_A={1,2,3,4,5,6,7}
set_B={4,5,6,7,8,9,10}
set_C=set_A.union(set_B) # set_A | set_B
print(set_C) 

#isdisjoint - It returns True if both sets are empty or both sets contain non-matching elements
print(set_A.isdisjoint(set_B))

#issubset - returns true if set_A is subset of set_B - "<=" is an abbrevation for subset
print(set_A.issubset(set_B)) # set_A <= set_B

#intersection - it returns only common elements from both sets '&' is abbrevation for intersection
print(set_A.intersection(set_B)) # set_A & set_B

#intersection_update - it keeps elements in first set which are matched with second set   
set_1={1,2,3,4,5}
set_2={1,2,3,4,5,6,7}

print(set_1)
print(set_2)

set_1.intersection_update(set_2)

print('set_1 updated with elements matched :',set_1)


#Difference - it returns all elements from first set which are not there in second set
print(set_A.difference(set_B)) #set_A - set_B

#symmetric_difference - it returns un-matching elements from both sets
print(set_A.symmetric_difference(set_B))

#Difference_update - it keeps elements in first set which are not matched with second set
set_A={'a','b','c','d'}
set_B={'c','d','e','f'}

print(set_A)
print(set_B)

set_A.difference_update(set_B)
print('set_A updated with non matched elements :', set_A)

#symmetric_difference_update - it will store un-matching elements from both sets into first set
set_C={'a','b',1,2,'c'}
set_D={'d','e','f',3,4,1,2}

set_C.symmetric_difference_update(set_D)

print(set_C)

#using set in list
list1=[10,20,30,{True,2,False,3},[40,2,{100,200,300}]]
print(list1[3])
#list1[3][0] #==> yhrows error since set don't support index

print(list1[0:4])
print(list1[0:list1[4][1]]) #list1[0:2]
