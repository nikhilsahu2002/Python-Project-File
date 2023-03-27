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

