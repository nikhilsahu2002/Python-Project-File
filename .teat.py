arr = [1,2,1,3,2]
d = 3
m = 2

for i in range(0,len(arr)-1):
        if(arr[i+1]+arr[i]==d):
            print(arr[i]+arr[i])
            break
        else :
              print(0)
              break

