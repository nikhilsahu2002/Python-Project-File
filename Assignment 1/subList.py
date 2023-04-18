l = list((input("Enter The String ")))
# after ADDing And Creating A New  List Of It Middle three Element 

mid = int(len(l)/2)

new_list= []
if mid%2==0:
    new_list.append(l[mid])
    new_list.append(l[mid+1])
    new_list.append(l[mid+2])
else:
    new_list.append(l[mid-1])
    new_list.append(l[mid])
    new_list.append(l[mid +1])

print(new_list)
