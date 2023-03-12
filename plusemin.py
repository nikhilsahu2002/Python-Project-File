ar=[1,1,0,-1,-1]
count =0
x=y=z=a=b=c=0
for i in range(0,len(ar)):
    if ar[i] >0:
        x=x+1
    elif ar[i]<0:
        y = y+1
    else:
        z=z+1

    a=x/len(ar)
    b=y/len(ar)
    c=z/len(ar)

print(a,b,c)
    

    # print(count)


