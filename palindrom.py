st = input("Enter The String")
c=[]

k = st.split()
# print(k) 
# print(c)
for i in range(0,len(k)):
    j=k[i]
    v =list(j)
    c = list(j)
    j= c.reverse()
    # print(v)
    for o in range(0,len(k)):
        n=k[o]  
    m = list(n) 
    # print(c)
    # print(m)

    for g in range(0,len(k)):
        if(c[g]=='a' or c[g]=='i' or c[g]=='o' or c[g]== 'e' or c[g]=='u' or v[g]=='a' or v[g]=='o' or v[g]=='i' or v[g]=='e' or v[g]=='u'): 
            print(f"vowel {c[g] or m[g]}")   
       

for o in range(0,len(n)):
    if(c[o]==n[o] and v[o]==n[o]):
        flag=0
    else:
        flag=1

if(flag==0):
    print("plindrom yes")
else :
    print("pilenrom no")


