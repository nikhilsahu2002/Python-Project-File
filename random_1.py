# random module: for handling randomization 
# return random float number between 0.0 to 1.0
import random

# print(random.random())

# # randan ont  returns random integers it between the specified range 
# print(random.randint(1,100)) 
# # retuens random elemnt created from start,stop,step are limite
# print(random.randrange(1,10))
# # return a randomely selected element from a sequence object such as string tuple and list 
# # 
# # math module  
# # sys model this model provide persantily related to python runtime envoirment 
# #  sys.argv[] - return list of commant line argguments passed to a python scripat
# # this module end the program and return to either python console and commond promte
# # sys.maxsize it returns the largest integer a variable can take 

i=chr(random.randint(33,47))
j=chr(random.randint(48,57))
k=chr(random.randint(58,64))
m=chr(random.randint(65,90))
l=chr(random.randint(97,122))
list1 = [i,j,k,m,l]

print(list1)
