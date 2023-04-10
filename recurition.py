# import sys
# sys.setrecursionlimit(2000)

# print(sys.getrecursionlimit())

#non -tail recursion
def fac(n):
    if(n<0):
        return print("not posible")
    elif(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return n * fac(n-1)
    
print(f"Factorial is {fac(5)}")

# tail recruion
def fac1(n,a=1):
    if(n<0):
        return print("not posible")
    elif(n==1):
        return a
    elif(n==0):
        return a
    else:
        return  fac1(n-1,n*a)
    


print(f"Factorial is {fac1(5)}")

# def num(n):
    
#     if n==0:
#         print(0) 
#     else:
#          (num(n-1))
#          print(n)


# x=num(5)

#fibonacci series
def feb(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
        return feb(n-2) + feb(n-1)
    
num = int(input("Enter The Range"))
for i in range(0,num):
    print(feb(i),end=' ')








