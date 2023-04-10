# import sys
# sys.setrecursionlimit(2000)

# print(sys.getrecursionlimit())


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

def num(n):
    
    if n==0:
        print(0) 
    else:
         (num(n-1))
         print(n)

num(5)

