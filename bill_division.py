def bonAppetit(bill, k, b):
    num =0
    for i in bill:
        if i != bill[1]:
            num=num+i
        
    num= int(num/2) 
    print(num)
    if num<b:
            print(abs(num-b))
    else:
            print("Bon Appetit")

bonAppetit([72 ,53 ,60 ,66 ,90 ,62 ,12 ,31 ,36 ,94],0,288)