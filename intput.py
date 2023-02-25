k =int((input("Enter The Value ")))

j =int(input("Enter The Secound Value "))

v =input("Enter The Opration To Perform ")

if (v == '+'):
    NUM =k+j
elif(v=='-'):
    NUM = k-j
elif(v=='/'):
    NUM =k/j
elif(v=='%'):
    NUM=k%j

print("The Result Is ",NUM)