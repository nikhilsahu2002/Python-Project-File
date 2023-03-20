def kangaroo(x1, v1, x2, v2):
    y = x1 + v1 
    z = x2 + v2
    
    for i in range(0,10):
        if(y!=z):
            y = y + v1
            z = z + v2
            
        if(y == z):
            print("YES")
            break
        else:
            print("No")
            break

kangaroo(14,4,98,2)