list1 = "P@#yn26at^&i5ve"

charater =0
Digit =0
Sybol =0

for i in list1:
    if i.isalpha():
        charater +=1
    elif i.isdigit():
        Digit +=1
    else:
        Sybol +=1

print(charater)
print(Digit)
print(Sybol)