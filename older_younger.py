age1 = 18
age2 = 25
age3 = 12

if(age1>age2 and age1>age3):
    print("Oldest = ",end=" ")
    print(age1)

elif(age2>age1 and age2>age3):
    print("Oldest = ",end=" ")
    print(age2)

else:
    print("Oldest = ",end=" ")
    print(age3)

if(age1<age2 and age1<age3):
    print("Youngest = ",end=" ")
    print(age1)

elif(age2<age1 and age2<age3):
    print("Youngest = ",end=" ")
    print(age2)

else:
    print("Youngest = ",end=" ")
    print(age3)

