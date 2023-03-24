def partinon(arr,low,high):
    pi = arr[high]

    i = low -1
    for j in range(low,high):
        count=0
        if arr[j] <= pi:
            i = i +1 
            (arr[i],arr[j]) = (arr[j],arr[i])
            count = count +1
    (arr[i+1] ,arr[high]) = (arr[high],arr[i+1])
    print(count)
    return i+1
    

def sort(arr,low,high):
    
    if low < high:
        pi =partinon(arr,low,high)
        sort(arr,low,pi-1)
        sort(arr,pi +1,high)
        


array = [8,7,2,1,0,9,6]

sort(array,0,len(array) - 1)
print(array)