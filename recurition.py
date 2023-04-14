# import sys
# sys.setrecursionlimit(2000)

# print(sys.getrecursionlimit())

# #non -tail recursion
# def fac(n):
#     if(n<0):
#         return print("not posible")
#     elif(n==1):
#         return 1
#     elif(n==0):
#         return 1
#     else:
#         return n * fac(n-1)
    
# print(f"Factorial is {fac(5)}")

# # tail recruion
# def fac1(n,a=1):
#     if(n<0):
#         return print("not posible")
#     elif(n==1):
#         return a
#     elif(n==0):
#         return a
#     else:
#         return  fac1(n-1,n*a)
    


# print(f"Factorial is {fac1(5)}")

def num(n):
    
    if n==0:
        return 0
    else:
         
         return n + num(n-1)


x=num(5)
print(x)

#fibonacci series
def feb(n,a=0,b=1):
    if(n==0):
        return a
    elif n==1:
        return b
    else:
        return feb(n-1,b,a+b)
    
# nums = int(input("Enter The Range"))
# for i in range(0,num):
#     print(feb(i),end=' ')

print(feb(5))


def fibonacci(n: int, a: int, b: int) -> int:
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1, b, a+b)

n = int(input("Enter the value of n: "))
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(fibonacci(n, a, b))


