def hcf (a, b):
    j=max(a,b)
    for i in range(1,j):
        if a%i==0 and b%i==0:
            HCF=i
    return HCF

def LCM(a,b):
    j=max(a,b)
    for i in range(1,j):
        if a%i==0 and b%i==0:
            hcf=i

        lcm=(a*b)/hcf
    return int(lcm)

print(hcf(20,30))
print(LCM(20,30))