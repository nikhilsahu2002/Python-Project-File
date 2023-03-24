def hcf (a, b):
    j=max(a,b)
    for i in range(1,j):
        if a%i==0 and b%i==0:
            HCF=i
        
    return HCF


print(hcf(20,30)),