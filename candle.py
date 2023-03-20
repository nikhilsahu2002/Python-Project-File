    # Write your code here

candles =[4]
num = max(candles)
j =len(candles)
count=0
for i in range(0,len(candles)):
    if (num==candles[i] and j!=1):
        count = count + 1
        

print(count)



    