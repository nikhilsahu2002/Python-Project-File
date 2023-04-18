list1 =list("America")
list2 = list("Japan")

mid1 = int(len(list1)/2)
mid2 = int(len(list2)/2)
def name(list1,list2):
    return list1[0]+list2[0] + list1[mid1] + list2[mid2] + list1[-1] + list2[-1]

print(name(list1,list2))