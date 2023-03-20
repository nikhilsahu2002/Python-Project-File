l=[4,8,3,8]
g=[]
le=[]
# [3,4,8,8]
for j in l:
    g.append(j)
g.sort()
print(l)
print(g)
print(len(l))
for i in range(0,len(l)):
    for j in range(0,len(g)):
        if(l[i]==g[j]):
            le.append(j + 1)
            break
           

print(le)
            







