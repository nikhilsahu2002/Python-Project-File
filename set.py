#set data type

# set are used to store multiple data item 
# unorderd data type 
# immutable (parseal-only add and remove method are allowed)
# no duplicate values are allowed
# enclosed by{} 

s ={5,5,3,'name','data'}
print(type(s))
s.add("age")

x =set((69,658,85,12,5)) #only can hold at least one arg... 
print(x)
print(s)

# y=s.issubset(x)
# print(y)

# frozen set its immutable (can't Be chnaged )

y=frozenset(s)



print(type(y))