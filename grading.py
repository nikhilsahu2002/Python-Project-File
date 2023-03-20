grade = [4,73,67,38,33]



for i in range(0,len(grade)):
        for j in range(0,100,5):
            k=grade[i]
            a=k-j
            if(k>40):
                if(a <3):
                    print(j)
                    break
                
