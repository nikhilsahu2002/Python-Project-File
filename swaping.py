list1 =[1,2,3,4,5]
list2 =[5,4,3,2,1]

for i in range(0,len(list1)):
    temp = list1[i]
    list1[i]=list2[i]
    list2[i]=temp

print(list2)