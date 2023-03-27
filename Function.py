# # # function:
# #     -is a block of code which only executes when it is called
# #     -pass : NULL Statment /Empty Statement 
# #     -we can pass a data into a function know as parameter
# #     -a function can return data as a result

# def show():
#     print("hello world")

# def add(a,b):
#     print(f"Sum Of {a} and {b} is {a+b}")

# def mul(a,b):
#     return a*b 

# def name():
#     return print("Nikhil")

# add(10,20)
# add(a=5,b=5)
# print(mul(2,3))

#paramenter vs Argument 
# a parameter is the variable listed inside the concnet defination '()' 
# an argument is the value that is sent to the function when it is called 

def add(a,b):
        return print(a+b)

def sub(a,b):
        print(a-b)
    
def mul(a,b):
        print(a*b)

def div(a,b=5):
        print(a//b)
#non default argument follows default argument 
# def new(a='',b):
#         print(a,b)

# funtion with arbitatrary argument
    # -variable lenth argument 
    # - * variable lenth arugment

# def sum(*info):
#         j=0
#         for i in info:
#                 j+=i
    
#         return j
          

# print(sum(4,2,9,45,24,74))

# - **Kwargs - key word based arbitrary argumnets

# def show(**info):
#         for key,value in info.items():
#                 print(key,value)

# show(name="nikhil",Class="MCA",age=22)

# def show(F):
#         for i in F:
#                 print(i)
# F=['banan','apple','orenga']
# g=show(F)

# def feb(args):
#             if(args==0):
#                     return args
#             elif(args==1):
#                     return args
#             else:
#                     return feb(args-2) + feb(args-1)
            
        
# for i in range(0,5):
#     print(feb(i))


# def fact(args):
        
#         if args ==0:
#                 return 1
#         else :
#                 return args*fact(args-1)

# print(fact(50))

# def value():
#         return 5

# n = value

# print(n())

#lamada funciton 
x= lambda a,b:a*b

z=x(5,10)
print(z)
