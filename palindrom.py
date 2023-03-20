st = input("Enter The String")
c=[]

k = st.split()
print(k) 
for i in range(0,len(k)):
    j=k[i]
c = list(j)
j= c.reverse()
# print(j)
for o in range(0,len(k)):
    n=k[o]
m = list(n)
print(c)
print(m)

for o in range(0,len(n)):
    if(c[o]==n[o]):
        flag=0
    else:
        flag=1

if(flag==0):
    print("plindrom yes")
else :
    print("pilenrom no")


