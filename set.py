#set data type

# set are used to store multiple data item 
# unorderd data type 
# immutable (parseal-only add and remove method are allowed)
# no duplicate values are allowed
# enclosed by{} 

s ={5,5,3,'name','data'}
# print(type(s))
s.add("age")

x =set((69,658,85,12,5)) #only can hold at least one arg... 
# print(x)
# print(s)

# y=s.issubset(x)
# print(y)

# frozen set its immutable (can't Be chnaged )

y=frozenset(s)
z=set()
size = int(input())
for i in range(0,size):
  k=int(input())
  z.add(k)
print(z)  



# print(type(y))

x = {10,20,30,40}
y = {20,40,60,70,80}

# print(x.difference(y))
# print(y.difference(x))
# print(x.union(y))
# x.update(y)
# x.update(5) Not Itrable 
# x.pop() Remove an Random Item 
# x.remove(100) remove method rase an error if item does not exist
# x.discard(200) does not rase an error if item does not exist  

# print(x.intersection(y))  return common item 
