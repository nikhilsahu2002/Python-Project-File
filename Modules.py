# module is a file that contains code to perform a specific task
# a module may contain variable function classes etc 
# as our programm gose bigger it may contains many lines of the code instade of putting everything into a single file use modules to seprate files as per 
# there functionalty.this make our code organzied and easyer to maintain 

# Types of Modules :
    # Build in Modules:
        # math
        # Os
        # sys
        # plateform
        # date and time 
        # Random  
        # Statictics 
    # User Difine Modules:
        #  Add
        #  Sum
#   Modules 
import bubble as c

def Sum(*s):
    j=0
    for i in s:
        j+=i
    return j

k=0
for i in range(10):
    k +=Sum(i)

# print(k)



# import statment 
'''
imorts statment import code from one module into another programm 
    syntex : import Module name 
    Example : c.BUBBLE(arr=[5,1,58,24,36])


    Aliasing - Assign a nickname 
    Example : method as nickname
            : bubble.BUBBLE as c

    form import statement : To Load A Specific Function From A Module
        from modulename import fuction1 ,function2 
    import heapSort 

    arr=[21,52,14,36,74,85]
    heapSort.heapsort(arr)

    for i in arr:
        print(i)

    os module: Provides Function For Operting 
        System Task 
        - Creating and Removing a Directory 
        - Fetching its contant 
        - Changing and idenfiy Current Working Dirctory 

        # getcwd() - return current working directory

        import os
        print(os.getcwd())
        os.mkdir("MODULE") 
'''

