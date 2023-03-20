def divisibleSumPairs(n, k, ar):
    # Write your code here
    count=0
    for j in range(0,n-1):
        for i in range(j+1,n):
            f = ar[i] + ar[j]
            if(f% k== 0):
                count+=1
    
    print(count)

divisibleSumPairs(6,3,[1,3,2,6,1,2])