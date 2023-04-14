#swapping max to min element 

arr=[10,2,10,85,12,10]

# for i in arr:
#     if i == 10:
#         arr.remove(i)

print(arr)
Max=max(arr)
Min = min(arr)

for i in range(0,len(arr)):
    if arr[i]==Max:
        arr[i]=Min
    elif arr[i]==Min:
        arr[i]=Max

print(arr)
