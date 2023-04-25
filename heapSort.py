def heaipiy(arr,n,i):
    larger = i 
    left = 2*i +1
    right = 2*i +2

    if left<n and arr[larger]<arr[left]:
        larger =left
    if right <n and arr[larger]<arr[right]:
        larger = right

    if larger != i:
        arr[i], arr[larger] = arr[larger], arr[i]
        heaipiy(arr,n,larger)
    
def heapsort(arr):
    n=(len(arr))
    for i in range(n//2 - 1,-1,-1):
        heaipiy(arr,n,i)
    
    for i in range(n-1,0,-1):
        temp = arr[0]
        arr[0]=arr[i]
        arr[i]=temp
        heaipiy(arr,i,0)
    

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
 
    # Function call
    heapsort(arr)
    N = len(arr)
 
    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")