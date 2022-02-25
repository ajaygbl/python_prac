"""
dictionary is an unordered set of key,value pairs, here keys are unique
dictionary keys are immutable, values are mutable
dictionary will not allow index,slicing
dictionary indexed by keys

"""

dict1={} #empty dict

dict1['a']=1
dict1['b']=2
dict1['c']=3

print(dict1)

print('#updating value of a key in dict')
dict1['a']=4
print(dict1)

print('#creating dict with dict() func')
dict2=dict([('a',10),('b',22),('c',30)])
print(dict2)

print('#creating dict with curl braces')
dict3={'d':3,'e':5,'f':6}
print(dict3)

print('#Access data from dict')
students = {'Name':'Joy','Marks':45,'Class':10,'Age':15,'Subjects':['social','english','Telugu']}
print(students['Name'])
print(students['Subjects'][0])

print('#Check')
print('Age' in students)

print('#Add new key:value in the existing dict')
dict3['g']=10
print(dict3)

print('#update value in dict')
dict3['g']=20
print(dict3)

print('#delete key:value pair using pop')
students.pop('Marks')
print(students)

print('#delete key:value using del')
del students['Name']
print(students)
del students #deletes whole dictionary
#print(students) --> throws an error


print('#fromkeys() -- we can use tuple as keys in dict & elements must be unique')
tup=(1,2,3,4,5)

dict1={}.fromkeys(tup)
print(dict1)

dict1={}.fromkeys(tup,'apple')
print(dict1)

print('#using tuple as key') 
dict_tup={(1,2,3,4,5):'1 to 5 numbers',2:'two'}
print(dict_tup[(1,2,3,4,5)])

print('#fromkeys() -- we can use List as keys in dict')
lst=['a1','b1','c1','a1'] #--dict takes no repeated element it just ignores it
dict_lst={}.fromkeys(lst)
print(dict_lst)
#we can't use list as key in dict
#dict_lst={[1,2,3,4,5]:'apple',2:'two'}

#update()
d={'fruit':'apple'}
d1={'animal':'tiger'}

d.update(d1)
print(d) # d={'fruits':'apple','animal':'tiger'}

#items() - it is used to get all items & it shows key:value in tuple format
print(d.items())

print('#creating dictionary of dictionaries')
emp1={'name':'john','age':20,'location':'newyork'}
emp2={'name':'mahesh','age':21,'location':'delhi'}

emps={'emp1':emp1,'emp2':emp2}

print(emps)

print('#Iterating over dict')
emp={'id':1001,'name':'sai','age':10,'location':'delhi',100:1000}

for i in emp:
        print(i,":",emp[i])
            
                
                    
print('#Nested dictionary')
emps={1001:{'name':'abdul','age':25,'skill':'python'},1002:{'name':'anand','age':25,'skill':'linux'},1003:{'name':'jade','age':24,'skill':'java'}}
print(emps[1001]['name'])
print(emps[1002]['name'])
print(emps[1003]['name'])

#iterating over dict object
for empid,empinfo in emps.items():
    print('empid: ',empid)
    print('empinfo: ',empinfo)
    
print('#Max, Min, Len of dict values')
d1={'val1':10,'val2':20,'val3':30,'val4':40}
print(max(d1.values()))
print(min(d1.values()))
print(len(d1.values()))
