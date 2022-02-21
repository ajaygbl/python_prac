#LIST

list1=list('python')
list2=list(range(10))
print(list1,list2)

list3=[10,20,30,40,50,60,70]
print(list3[3:7])

list4=list1+list2
print(list4)

print("\n")
print("###################################")
print("##########NESTED_LIST##############")
print("\n")

#Nested List
list5=[1,2,3,4,['python','ruby'],5,6,7,8]
print(list5[4])
print(list5[4].index('python'))

print("###################################")
print("###################################")
print("\n")

list6=[1,2,3,4,[10,20,30,40,[100,200,300,400],50,60],5,6]
print(list6[4][0])
print(list6[4][4])
print(list6[4][4][0])

print("\n")
print("###################################")
print("##################APPEND###########")
print("\n")

#append()
list6.append(50)
list6[4][4].append(500)
print(list6)

print("\n")
print("###################################")
print("##############EXTEND###############")
print("\n")

#extend()
list2.extend([80,90,100])
print(list2)

print("\n")
print("###################################")
print("############INSERT##################")
print("\n")

#Insert
list2.insert(3,'python')
print(list2)

print("\n")
print("###################################")
print("################REMOVE#############")
print("\n")

#Remove -- It removes by specifying element
list2.remove('python')
print(list2)

print("\n")
print("###################################")
print("##################POP##############")
print("\n")


#pop -- It removes by specifying index
list2.pop(2)
print(list2)
#if you dont specify index it removes last element
list2.pop() 
print(list2)

print("\n")
print("###################################")
print("#################REVERSE###########")
print("\n")

#Reverse
list2.reverse()
print(list2)

print("\n")
print("###################################")
print("#################COPY##############")
print("\n")

#copy
x_list=list2.copy()
print(x_list)

print("\n")
print("###################################")
print("####################CLEAR##########")
print("\n")

#clear
x_list.clear()
print(list2)


#CONERSIONS
print("####CONVERTING STRING TO LIST####")
print("\n")

str1="PYTHON IS VERY USEFUL"
list_str=str1.split()
print(list_str)

print("\n")
print("####CONVERTING LIST TO STRING####")
print("\n")

str2=" ".join(list_str)
print(str2)

print("\n")
print("####add letter to string####")
print("\n")

str2 = str2+'s'
print(str2)
